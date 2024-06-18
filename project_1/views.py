
from django.http import HttpResponse

def contact (request):
    return HttpResponse("This is contact page")


def home (request):
    
    return HttpResponse("This is home page")



def about(res) :
    
    name = "My name is Adnan"
    fci = "My campus name is feni computer insttitute"
    
    return HttpResponse({name ,fci})

