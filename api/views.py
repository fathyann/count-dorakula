from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Queue, Retry, Top
import json

# Create your views here.
@csrf_exempt
def register(request):
  if request.method == 'POST':
    name = request.POST['name']
    last = Queue.objects.create(name=name)
    last.number = last.pk
    last.save()
    response = {
      'id' : last.number,
      'name' : last.name
    }
    return JsonResponse(response, safe=False)
  else:
    return JsonResponse({'error':'POST only'}, safe=False, status=400)

def get_top(request):
  if Top.objects.count() != 0:
    top = Top.objects.first()
    response = {
      'id' : top.number,
      'name' : top.name
    }
    return JsonResponse(response, safe=False)
  else:
    return JsonResponse({'error':'no data'}, safe=False, status=400)

@csrf_exempt
def pop_queue(request):
  if request.method == 'POST':
    if(Queue.objects.count() != 0):
      top = Queue.objects.first()
      Queue.objects.first().delete()
      if(Top.objects.count() != 0):
        Top.objects.first().delete()
      Top.objects.create(name=top.name, number=top.number)
      response = {
        'id' : top.number,
        'name' : top.name
      }
      return JsonResponse(response, safe=False)
    else:
      return JsonResponse({'error':'no data'}, status=400)
  else:
    return JsonResponse({'error':'POST Only'}, safe=False)

@csrf_exempt
def pop_retry(request):
  if request.method == 'POST':
    if(Retry.objects.count() != 0):
      top = Retry.objects.first()
      Retry.objects.first().delete()
      if(Top.objects.count() != 0):
        Top.objects.first().delete()
      Top.objects.create(name=top.name, number=top.number)
      response = {
        'id' : top.number,
        'name' : top.name
      }
      return JsonResponse(response, safe=False)
    else:
      return JsonResponse({'error':'no data'}, status=400)
  else:
    return JsonResponse({'error':'POST Only'}, safe=False, status=400)

@csrf_exempt
def requeue(request):
  if request.method == 'POST':
    top = Top.objects.first()
    last = Retry.objects.create(name=top.name, number=top.number)
    response = {
      'id' : last.number,
      'name' : last.name
    }
    return JsonResponse(response, safe=False)
  else:
    return JsonResponse({'error':'POST Only'}, safe=False)
