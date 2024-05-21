
from .ScientistsSerializer import RegisterSerializer, ScientistDetailSerializer, ScientistUpdateSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Scientist


class ScientistRegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            scientist = serializer.save()
            response_data = {
                "message": "Scientist registered successfully",
                "username": scientist.username,
                "author_in_russian": scientist.author_in_russian,
                "first_author": scientist.first_author,
                "job_title": scientist.job_title,
                "relations": scientist.relations,
                "science_title": scientist.science_title,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScientistDetailAPIView(APIView):
    def get(self, request, username):
        try:
            scientist = Scientist.objects.get(username=username)
            serializer = ScientistDetailSerializer(scientist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Scientist.DoesNotExist:
            return Response({"message": "need register"}, status=status.HTTP_404_NOT_FOUND)


class ScientistUpdateAPIView(APIView):
    def put(self, request, username):
        try:
            scientist = Scientist.objects.get(username=username)
        except Scientist.DoesNotExist:
            return Response({"message": "need register"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScientistUpdateSerializer(scientist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)