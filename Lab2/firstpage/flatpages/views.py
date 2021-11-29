from django.http import HttpResponse

def home(request):
    return HttpResponse(u'Hello, World!', content_type="text/plain")
