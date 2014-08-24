from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
  #return render(request, 'restoapp/index.html', {})
  context = RequestContext(request)
  return render_to_response('restoapp/index.html', {}, context)
