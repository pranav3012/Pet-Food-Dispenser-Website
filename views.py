from django.shortcuts import render
import pymongo

from django.http import HttpResponse
from .models import User_Data
 
myclient = pymongo.MongoClient("mongodb+srv://PFD:PFD123456@cluster0.vesoses.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["Sensor"]
mycol = mydb["Readings"]

def index(request):
    Parameter = User_Data()
    Parameter.DT_1 = (request.GET.get('para1_Time'))
    Parameter.DW_1 = (request.GET.get('para1_Weight'))
    
    Parameter.DT_2 = (request.GET.get('para2_Time'))
    Parameter.DW_2 = (request.GET.get('para2_Weight'))
    
    Parameter.DT_3 = (request.GET.get('para3_Time'))
    Parameter.DW_3 = (request.GET.get('para3_Weight'))
    print(Parameter.DT_1)
    print(Parameter.DW_1)
    
    print(Parameter.DT_2)
    print(Parameter.DW_2)
    
    print(Parameter.DT_3)
    print(Parameter.DW_3)
    # data_valuez = [Parameter]
    if Parameter.DT_1 and Parameter.DW_1 != 'NULL':
        mycol.update_many(
        {"_id":"30"},
        {
            "$set":{"Ti":Parameter.DT_1, "We":Parameter.DW_1}
        })
        mycol.update_many(
        {"_id":"03"},
        {
            "$set":{"CRP":'01'}
        })
    if Parameter.DT_2 and Parameter.DW_2 != 'NULL':
        mycol.update_many(
        {"_id":"40"},
        {
            "$set":{"Ti":Parameter.DT_2, "We":Parameter.DW_2}
        })
        mycol.update_many(
        {"_id":"03"},
        {
            "$set":{"CRP":'01'}
        })
    if Parameter.DT_3 and Parameter.DW_3 != 'NULL':
        mycol.update_many(
        {"_id":"50"},
        {
            "$set":{"Ti":Parameter.DT_3, "We":Parameter.DW_3}
        })
        mycol.update_many(
        {"_id":"03"},
        {
            "$set":{"CRP":'01'}
        })
        

    return render(request, "ask.html",)
    
 
#  return HttpResponse("Hello Geeks")
# Create your views here.
