from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
# Create your views here.
from myapp.models import Room
from myapp.models import Guess

def index(request):
  return HttpResponse('Hello world')

def room_to_dict(data):
  
  return {"id":data.id,"code":data.code,"num":data.num,"start":data.start}

def guess_to_dict(data):
  
  return {"id":data.id,"room_id":data.room_id.id,"info":data.info,"eat":data.eat,"bite":data.bite}


def getRooms(request):
  dbData = {
    "room":[],
  }
  objs = Room.objects.filter().all()
  for obj in objs:
    dbData["room"].append(room_to_dict(obj))
  return JsonResponse(dbData)

def getRoom(request):
  obj = Room.objects.get(id=request.GET["id"]);
  dbData = {
    "room":room_to_dict(obj),
  }
  return JsonResponse(dbData)

def getGuess(request):
  
  dbData = {
    "guess":[],
  }
  objs = Guess.objects.filter(room_id=request.GET['id']).all()
  for obj in objs:
    dbData["guess"].append(guess_to_dict(obj))
  return JsonResponse(dbData)

#　要求仕様
# roomを作る
# roomに入ったとき抜けたときに人数を編集
# room内が1人の場合抜けたときにルームを削除
# roomでゲームがスタートするとcodeとスタート時間が設定される
# 誰かが答えを入力するとguessテーブルにレコードが一つ追加される

def createRoom(request):
  Room(code="",num=0).save()#todo start
  return JsonResponse({"0":0})

def joinRoom(request):
  objs = {}
  print("a")
  if 'id' in request.GET:
    print("b")
    obj = Room.objects.get(id=request.GET['id'])
    Room(id = obj.id,num = obj.num+1,code=obj.code,start=obj.start).save()
  return JsonResponse({"説明":"idが必要"})

def leftRoom(request):
  if 'id' in request.GET:
    obj = Room.objects.get(id=request.GET['id'])
    if obj.num==0:
      return JsonResponse({"a":"0"})
    Room(id = obj.id,num = obj.num-1,code=obj.code,start=obj.start).save()
  return JsonResponse({"説明":"idが必要"})

def setCode(request):
  if 'id' in request.GET:
    obj = Room.objects.get(id=request.GET['id'])
    if 'code' in request.GET:
      Room(id = obj.id,num = obj.num,code=request.GET['code'],start=obj.start).save()
  return JsonResponse({"説明":"id,codeが必要"})

def setStart(request):
  if 'id' in request.GET:
    obj = Room.objects.get(id=request.GET['id'])
    if 'start' in request.GET:
      Room(id = obj.id,num = obj.num,code=obj.code,start=request.GET['start']).save()
  return JsonResponse({"説明":"id,startが必要"})
    
def createGuess(request):
  Guess(room_id=Room.objects.get(id=request.GET['room_id']),info=request.GET['info'],eat=request.GET['eat'],bite=request.GET['bite']).save()
  return JsonResponse({"説明":"room_id,info,eat,biteが必要"})

def deleteHistory(request):
  if 'id' in request.GET:
    objs = Guess.objects.filter(room_id=request.GET["id"]).all()
    for obj in objs:
      obj.delete()
  return JsonResponse({"a":0})