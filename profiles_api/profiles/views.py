from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
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


class HelloViewSet(viewsets.ViewSet):
    """test api view set"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses actions (list , create,retrieve,update,partial update)'
        ]
        return Response({'message':'hello','a_viewset':a_viewset})
    
    def create(self,request):
        """creates a new hello message"""
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return f'Hello {name}'
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,request,pk=None):
        """handles getting an object by Id"""
        return Response({'http_method':'GET'})
    
    def update(self, request,  pk=None):
        """Handle updating an Object"""
        return Response({'http_method':'Update and Object'})
    
    def partial_update(self, request,  pk=None):
        """Handle updating an Object"""
        return Response({'http_method':'partial Update and Object'})
    
    def destroy(self, request,  pk=None):
        """Handle updating an Object"""
        return Response({'http_method':'Delete'})