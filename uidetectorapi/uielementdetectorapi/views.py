import os
import time
import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import DetectionsSerializer
from .models import Detections
from .setups import DEMO_PATH,EXP_FILE,MODEL_PATH
from .YOLOX.tools.demo import main_detector,make_parser,get_exp
from .codewriter import json_reader,addUiElements



# Create your views here.


# TODO to be changed later
def path_converter(path):
    return path.replace("\\",'/')

class DetectionsViewSet(viewsets.ModelViewSet):
    queryset = Detections.objects.filter(id=1)
    serializer_class = DetectionsSerializer


    def create(self, request, *args, **kwargs):

        # Perform Transaction
        confidence = float(request.data['confidence'])
        image_to_detect = request.data['image_to_detect']

        detections = Detections.objects.create(image_to_detect=image_to_detect,confidence=confidence)
        VAL_IMG_PATH = f'media/{detections.image_to_detect}'

        # YOLOX PARAMETERS
        conf = confidence
        args = make_parser().parse_args()
        args.demo = "image"
        args.exp_file = EXP_FILE
        args.ckpt = MODEL_PATH
        args.path = VAL_IMG_PATH
        args.conf = conf
        args.nms = 0.45
        args.tsize = 640
        args.save_result = True
        exp = get_exp(args.exp_file, args.name)

        # YOLOX DETECTOR
        img,jfile = main_detector(exp,args)
        img,jfile = path_converter(img),path_converter(jfile)

        # PYQT CODE GENERATOR
        data = json_reader(jfile)

        height = data['image_height']
        width = data['image_width']
        bounds = data['bounds']
        classes = data['classes']
        classes_names = data['classes_names']
        image_name = data['image_name'].split(".")[0]
        save_dir = f'media/{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}'
        os.makedirs(save_dir,exist_ok=True)
        code_generated_path = f'{save_dir}/{image_name}.py'

        addUiElements(width,height,bounds,classes,classes_names,code_generated_path)

        return Response({
            'image_to_detect':  request.build_absolute_uri(VAL_IMG_PATH),
            'detected_image_path':request.build_absolute_uri(img),
            'code_generated': request.build_absolute_uri(code_generated_path),
            'json_file_path': request.build_absolute_uri(jfile)
        })














