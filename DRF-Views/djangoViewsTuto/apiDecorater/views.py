from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import LaptopModel
from .serializers import LaptopSerializer


"""[ @csrf_exempt ]set a CSRF (Cross-Site Request Forgery) cookie. 
This makes it possible to POST to this view from 
clients that won’t have a CSRF token."""
# @csrf_exempt

"""
List all LaptopModel, or create a new transformer
"""
# @csrf_exempt
@api_view(["GET", "POST"])
def laptopListCreate_apiView(request):
    if request.method == "GET":
        laptopsObject = LaptopModel.objects.all()
        serializerClass = LaptopSerializer(laptopsObject, many=True)
        return Response(serializerClass.data)

    elif request.method == "POST":
        serializerClass = LaptopSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data, status=status.HTTP_201_CREATED)
        return Response(serializerClass.data, status=status.HTTP_400_BAD_REQUEST)    


"""
Retrieve, Update, Patch Update and Delete a LaptopModel's instance
"""
@api_view(["GET", "PUT", "PATCH", "DELETE"])
# @csrf_exempt
def laptopDetail_apiView(request, pk):
    
    # """Method 1 using Try"""
    # try:
    #     laptopObj = LaptopModel.objects.get(pk=pk)
    # except LaptopModel.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)


    """Method 1 using Try with error code mesage"""
    try:
        laptopObj = LaptopModel.objects.get(pk=pk)
    except LaptopModel.DoesNotExist:
        return Response({"error": {"code" :404, "message": "Laptop not found!"}}, status=status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
        serializerClass = LaptopSerializer(laptopObj)     
        return Response(serializerClass.data)

    elif request.method == "PUT":
        serializerClass = LaptopSerializer(laptopObj, data=request.data)

        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)    
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":   
        serializerClass = LaptopSerializer(laptopObj, data=request.data, partial=True)

        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        laptopObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

             