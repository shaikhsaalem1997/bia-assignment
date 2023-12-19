from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import UserSerializer, MovieSerializer
import cv2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import os
import numpy as np


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("Invalid credentials", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, Django!'}
        return Response(content)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def create_frame_with_text(text, width, height):
    frame = cv2.putText(
        img=cv2.cvtColor(np.zeros((height, width, 3), dtype=np.uint8), cv2.COLOR_BGR2RGB), 
        text=text, 
        org=(50, 100), 
        fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
        fontScale=1, 
        color=(255, 255, 255),
        thickness=2, 
        lineType=cv2.LINE_AA
    )

    return frame


def generate_video():
    width, height = 640, 480  
    fps = 24  

    static_path = os.path.join(os.getcwd(), 'static')

    save_dir = os.path.join(static_path, 'processed_videos')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    output_path = os.path.join(save_dir, 'generated_video.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for i in range(100): 
        frame = create_frame_with_text("Processd sample text-to-video.", width, height)
        out.write(frame)

    out.release()
    return output_path


@api_view(['GET'])
def process_video(request):
    if request.method == 'GET':
        saved_path = generate_video()
        return Response({'message': 'Video generation successful at ' + saved_path}, status=200)
    else:
        return Response({'message': 'Invalid request'}, status=400)


