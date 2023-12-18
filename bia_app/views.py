from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer
import cv2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import os
import numpy as np


def hello_django(request):
    return HttpResponse("Hello, Django!")


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


