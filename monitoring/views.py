from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to my web site")