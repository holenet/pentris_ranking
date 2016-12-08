from django.shortcuts import render
from .models import Score
from django.http import HttpResponseBadRequest, HttpResponse
from django.utils import timezone
from random import randint
from django.views.decorators.csrf import csrf_exempt

interval = 10
bits = 31


def is_post_data_valid(t):
    check = ['score', 'username']
    for x in check:
        if x not in t:
            return False
    return True


def encrypt(c):
    global interval, bits
    s = ''
    print(range(bits*interval-1,-1,-1))
    for i in range(bits*interval-1,-1,-1):
        if i%interval<interval-1:
            s = chr(48+17*randint(0,4)+randint(0,7)+2)+s
        else:
            s = chr(48+17*randint(0,4)+c%2)+s
            c //= 2
    return s


def decrypt(s):
    global interval, bits
    l = len(s)
    if l != interval * bits:
        return -1
    c = 0
    for i in range(l):
        if i % interval < interval-1:
            continue
        k = (ord(s[i])-48)%17
        if k>1:
            return -i-1000
        c *= 2
        c += k
    return c

# POST
@csrf_exempt
def submit(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    if not is_post_data_valid(request.POST):
        return HttpResponseBadRequest()

    decrypted = decrypt(request.POST['score'])
    if decrypted < 0:
        return HttpResponseBadRequest()

    new_score = Score(
        score=decrypted,
        username=request.POST['username'],
        submit_date=timezone.now(),
    )
    new_score.save()

    return HttpResponse()
