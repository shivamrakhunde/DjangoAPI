from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'image_api/index.html', {})

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})