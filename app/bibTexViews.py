from django.db.models.functions import Trim
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .bibTexSerializers import BibTexSerializer, BibTexUpdateSerializer
from .models import BibText, User


class BibTexUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BibTexSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BibTexListView(APIView):
    def get(self, request):
        bibtex_entries = BibText.objects.all()
        serializer = BibTexSerializer(bibtex_entries, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BibTexByAuthorListView(APIView):
    def get(self, request, author_name):
        bibtex_entries = BibText.objects.annotate(
            trimmed_author=Trim('author')
        ).filter(trimmed_author__iexact=author_name.strip())

        if not bibtex_entries.exists():
            return Response({'message': 'No entries found for this author'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BibTexSerializer(bibtex_entries, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BibTexByUserListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        bibtex_entries = BibText.objects.filter(username=username)
        serializer = BibTexSerializer(bibtex_entries, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BibTexByDOIView(APIView):
    def get(self, request, doi,username):
        try:
            bibtex_entry = BibText.objects.get(doi=doi,username=username)
            serializer = BibTexSerializer(bibtex_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BibText.DoesNotExist:
            return Response({'message': 'BibText with this DOI not found'}, status=status.HTTP_404_NOT_FOUND)


class AuthorListView(APIView):
    def get(self, request):
        authors = BibText.objects.values_list('author', flat=True).distinct().order_by('author')
        return Response({'authors': list(authors)}, status=status.HTTP_200_OK)


class UncheckedBibTexView(APIView):
    def get(self, request, username):
        entries = BibText.objects.filter(username=username, checked=0)
        serializer = BibTexSerializer(entries, many=True)
        return Response(serializer.data)


class CheckedBibTexView(APIView):
    def get(self, request, username):
        entries = BibText.objects.filter(username=username, checked=1)
        serializer = BibTexSerializer(entries, many=True)
        return Response(serializer.data)


from django.shortcuts import get_object_or_404


class BibTexUploadAndCheckView(APIView):
    def patch(self, request, pk):
        bibtext_instance = get_object_or_404(BibText, pk=pk)
        print(request.data)
        serializer = BibTexUpdateSerializer(bibtext_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
