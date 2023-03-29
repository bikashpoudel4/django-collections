from rest_framework import generics

from .models import PhoneModel
from .serializers import PhoneSerializer

from rest_framework.response import Response
from rest_framework import status

# Lists all the data and Post all the data [GET, POST] Method
class PhoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneSerializer
    
class PhoneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneSerializer
    
    # # Writing Responses 
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)