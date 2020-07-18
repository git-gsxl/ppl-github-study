from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def hello_demo(request):

    return HttpResponse('hello word!')

def json_demo(request,name,phone):

    json = {
        "code": 1,
        "msg": "success!",
        "data": [{
            "name": name,
            "phone": phone
        }]
    }

    return JsonResponse(json)

def login_demo(request):
    return render(request, 'login.study_html')
