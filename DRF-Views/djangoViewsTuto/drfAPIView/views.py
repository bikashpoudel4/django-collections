from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView

from .serializers import NoteSerializer
from .models import NoteModel

#---------------------- DRF APIView  EXAMPLE ---- also called CLASS BASED APIView ------------------------------------
# EG 1 **************************************************************

"""
  List all Notes, or create a new Note
"""
class NoteListCreateAPIView(APIView):

    # get method
    def get(self, request):
        # creating note object
        notesObject = NoteModel.objects.all()
        serializerClass = NoteSerializer(notesObject, many=True) #many=True is essentiaol here
        return Response(serializerClass.data)

    def post(self, requset): #also called save mtyhod
        serializerClass = NoteSerializer(data=requset.data)

        if serializerClass.is_valid():
            serializerClass.save()
            # If data is valid and saved return response it as created
            return Response(serializerClass.dat, status=status.HTTP_201_CREATED)
        # if data is invalid return response badRequest
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST) 


"""
Retrieve, Update, Patch Update and Delete a Note's instance
"""
class NoteDetailAPIView(APIView):
    
    """Method 1 using try catch for get_object"""
    # def get_object(self, pk):
    #     # Returns an object instance that should
    #     # be used for detail
    #     try:
    #         return Note.objects.get(pk=pk)
    #     except Note.DoesNotExist:
    #         raise Http404    


    # """Method 2 for get_object"""
    def get_object(self,pk):
        noteObj = get_object_or_404(NoteModel, pk=pk)
        return noteObj


    def get(self, request, pk):
        noteObj = self.get_object(pk)
        serializerClass = NoteSerializer(noteObj)
        return Response(serializerClass.data)

    def put(self, request, pk):
        noteObj = self.get_object(pk)
        serializerClass = NoteSerializer(noteObj, data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    def patch(self, request, pk):
        noteObj = self.get_object(pk)
        serializerClass = NoteSerializer(noteObj, data=request.data, partial=True)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        noteObj = self.get_object(pk)
        noteObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
