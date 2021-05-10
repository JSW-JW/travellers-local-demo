from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import TokenAuthentication

from diary import serializers
from diary.models import Diary
from rest_framework.generics import get_object_or_404


class DiaryCreateListAPIView(APIView):

    parser_classes = [MultiPartParser,]
    serializer_class = serializers.DiarySerializer
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        """Returns a list of APIView features"""
        diaries = Diary.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            diaries = diaries.filter(title__icontains=title)

        serializer = serializers.DiarySerializer(diaries, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.DiarySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            diary = serializer.save(user=request.user)
            images = dict((request.data).lists())['image_set']
            if images != None:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        """Image creation process and making connections"""
        # images = dict((request.data).lists())['image_set']
        # print('image_set', images)
        # arr = []
        # for img_name in images:
        #     modified_data = modify_input_for_multiple_files(img_name)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiaryDetailAPIView(APIView):

    def get_object(self, pk):
        diary = get_object_or_404(Diary, pk=pk)
        return diary

    def get(self, request, pk):
        diary = self.get_object(pk)
        serializer = serializers.DiarySerializer(diary, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        diary = self.get_object(pk)
        serializer = serializers.DiarySerializer(diary, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        diary = self.get_object(pk=pk)
        diary.delete()
        return Response({'message': 'Diary was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
