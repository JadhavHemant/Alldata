from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from RestApp.DatabaseOperations import Operations

def CustomerPage(request):
    return render(request,"Customer.html")
# @api_view(["GET","POST","PUT","DELETE"])
# def ApiDemoView(request):
#     if(request.method=="GET"):
#         return JsonResponse({"rno":1,"name":"Ajay"},safe=False)
#     elif(request.method=="POST"):
#         return JsonResponse({"msg":"Welcome"},safe=False)



@api_view(["GET","POST","PUT","DELETE"])
def StudentApiView(request):
    op=Operations("localhost","root","","collegedb")
    if(request.method=="GET"):
        if 'rno' in request.GET:
            rno=int(request.GET["rno"])
            data=op.Execute("FetchByRno",rno,"",0,0,0)
            return JsonResponse(data,safe=False)
        else:
            data=op.Execute("FetchAll",0,"",0,0,0)
            return JsonResponse(data,safe=False)
    if(request.method=="POST"):
        data=JSONParser().parse(request)
        print(data['name'])
        ms=op.Execute("Insert",0,data["name"],data["english"],data["science"],data["maths"])
        return JsonResponse({"msg":ms})
