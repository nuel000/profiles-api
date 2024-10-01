from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles import serializers

class HelloApiView(APIView):
    """Testing API view"""
    serializer_class = serializers.HelloSerializer
    
    def get(self,request,format = None):
        """Returns a list of API view Features"""
        an_apiview = [
            'Uses HTPP method as a function (get,post,put,patch,put,delete)',
            'is similar to traditional Django View',
            'Gives You the most control over your application logic',
            'Is mapped manually to URLS'
        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request,format = None):
        """Create a hello message with name """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message':f'Hello {name}'})
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk = None):
        """Handles updating an entire object """
        return Response({'method':'PUT'})
    
    def patch(self,request,pk = None):
        """Handles a partial update of an object """
        return Response({'method':'PATCH'})
    
    
    def delete(self,request,pk = None):
        """Deletes an Object"""
        return Response({'method':'DELETE'})