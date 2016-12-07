from django.shortcuts import render
from submit.models import Score
from .models import API_log
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse, HttpResponseBadRequest
import json


@csrf_exempt
def response_by_json(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    new_log = API_log(
        remote_addr=request.META['REMOTE_ADDR'],
        submit_date=timezone.now(),
        success=True,
    )

    score_objects = Score.objects.all()[:100]
    queries = []

    for i, query in enumerate(score_objects):
        queries.append(
            {
                'rank': i+1,
                'score': query.score,
                'username': query.username,
                'submitted_date': str(query.submit_date),
            }
        )

    new_log.save()

    return HttpResponse(json.dumps(queries))
