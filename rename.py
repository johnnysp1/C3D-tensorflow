import cv2
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

video_path = 'datasets/ucf-101/'
action_list = os.listdir(video_path)
for action in action_list:
    video_list = os.listdir(video_path+action)
    for video in video_list:
        newname = video.split('_', 1)[1]
        os.rename(os.path.join(video_path+action+'/', video), os.path.join(video_path+action+'/', newname))

