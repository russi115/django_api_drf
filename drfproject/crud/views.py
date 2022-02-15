from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import boleto
from .serializers import BoletoSerializers
from .serializers import serializers

def root(request):
    return render(request, 'root.html')

def vticket(request):
    return render(request, 'vticket.html')

def crud(request):
    return render(request, 'crud.html')

@api_view(['GET'])
def validate(request, code=""):
    qr = boleto.objects.filter(code=code).values()
    serializers = BoletoSerializers(qr, many=True)
    if serializers.data[0]['usado'] == False:
        datos={'message':'Your ticket has not been used yet.'}
    else:
        datos={'message':'Your ticket has been used.'}
    return Response(datos)

@api_view(['GET'])
def getData(request,id=0):
    if (id>0):
        boletos=boleto.objects.filter(id=id).values()
        serializers = BoletoSerializers(boletos, many=True)
        return Response(serializers.data)
    else: 
        boletos = boleto.objects.all()
        serializers = BoletoSerializers(boletos, many=True)
        return Response(serializers.data)     

@api_view(['POST'])
def addItem(request):
    boletos = boleto.objects.filter(code=request.data['code']).values()
    if (len(boletos)>0):
        datos={"status": "error", "message": "El código ya existe"}
        return Response(datos)
    serializers = BoletoSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        datos={"message": "El boleto se ha guardado correctamente"}
    return Response(datos)

@api_view(['DELETE'])
def deleteItem(request,id):
    boletos=boleto.objects.filter(id=id).values()
    if len(boletos)>0:
        boleto.objects.filter(id=id).delete()
        datos={'message': 'Success'}
    else:
        datos={"message": "Boleto no encontrado"}
    return Response(datos)

@api_view(['PUT'])
def updateItem(request,id):
    boletos=boleto.objects.filter(id=id).values()
    if len(boletos)>0:
        boleto.objects.filter(id=id).update(code=request.data['code'],
                                            name=request.data['name'],
                                            usado=request.data['usado'],
                                            valor=request.data['valor'])
        datos={'message': 'Success'}
    else:
        datos={"message": "Boleto no encontrado"}
    return Response(datos)