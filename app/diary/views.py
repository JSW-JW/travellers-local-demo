from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from diary import serializers


@api_view(['GET', 'POST'])
def diary_list(request):
    if request.method == 'GET':
        diaries = Diary.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            diaries = diaries.filter(title__icontains=title)

        diary_serializer = serializers.DiarySerializer(diaries, many=True)
        return Response(diary_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            diary_serializer = serializers.DiarySerializer(data=request.data)
            if diary_serializer.is_valid():
                diary_serializer.save()
                return Response(diary_serializer.data, status=status.HTTP_201_CREATED)
            return Response(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: # if is_anonymous
            return Response({'message': 'Unauthenticated'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET', 'PUT', 'DELETE'])
def diary_detail(request, pk):
    try:
        diary = Tutorial.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return Response({'message': 'The diary does not exist'}, status=status.HTTP_404_NOT_FOUND)

    diary_serializer = serializers.DiarySerializer(diary)
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
