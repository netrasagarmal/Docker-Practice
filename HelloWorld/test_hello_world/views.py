from django.http import HttpResponse

def index(request):
    print("\n\n\t H e l l o  W o r l d from cmd\n\n")
    return HttpResponse("Hello World! from web browser")