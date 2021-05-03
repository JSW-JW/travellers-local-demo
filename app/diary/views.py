from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import TokenAuthentication

from diary import serializers
from diary.models import Diary
from diary.helpers import modify_input_for_multiple_files


# @api_view(['GET', 'POST'])
# def diary_list(request, filename):
#     parser_classes = [FileUploadParser]
#
#     if request.method == 'GET':
#         diaries = Diary.objects.all()
#
#         title = request.query_params.get('title', None)
#         if title is not None:
#             diaries = diaries.filter(title__icontains=title)
#
#         diary_serializer = serializers.DiarySerializer(diaries, many=True)
#         return Response(diary_serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#
#         if request.user.is_authenticated:
#             file_obj = request.data['file']
#
#             diary_serializer = serializers.DiarySerializer(data=request.data)
#             if diary_serializer.is_valid():
#                 diary_serializer.save()
#                 return Response(diary_serializer.data, status=status.HTTP_201_CREATED)
#             return Response(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else: # if is_anonymous
#             return Response({'message': 'Unauthenticated'}, status=status.HTTP_401_UNAUTHORIZED)

class DiaryView(APIView):
    parser_classes = [MultiPartParser,]
    serializer_class = serializers.DiarySerializer
    authentication_classes = (TokenAuthentication,)
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        diaries = Diary.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            diaries = diaries.filter(title__icontains=title)

        diary_serializer = serializers.DiarySerializer(diaries, many=True, context={'request': request})
        return Response(diary_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        diary_serializer = serializers.DiarySerializer(data=request.data, context={'request': request})
        images = dict((request.data).lists())['image_set']
        print('image_set', images)
        # arr = []
        # for img_name in images:
        #     modified_data = modify_input_for_multiple_files(img_name)
        if diary_serializer.is_valid():
            diary = diary_serializer.save(user=request.user)
            diary_serializer = serializers.DiarySerializer(diary)

            return Response(diary_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def diary_detail(request, pk):
    try:
        diary = Diary.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return Response({'message': 'The diary does not exist'}, status=status.HTTP_404_NOT_FOUND)

    diary_serializer = serializers.DiarySerializer(diary, context={'request': request})
    if request.method == 'GET':
        return Response(diary_serializer.data)

    elif request.method == 'PUT':
        if diary_serializer.is_valid():
            diary_serializer.save()
            return Response(diary_serializer.data, status=status.HTTP_200_OK)
        return Response(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diary.delete()
        return Response({'message': 'Diary was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
