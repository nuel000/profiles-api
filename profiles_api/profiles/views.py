from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Testing API view"""
    
    def get(self,request,format = None):
        """Returns a list of API view Features"""
        an_apiview = [
            'Uses HTPP method as a function (get,post,put,patch,put,delete)',
            'is similar to traditional Django View',
            'Gives You the most control over your application logic',
            'Is mapped manually to URLS'
        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
