import cv2
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

video_path = 'datasets/ucf-101/'
labelnum=-1
action_list = os.listdir(video_path)
f1 = open('ucfTrainTestlist/train_file.txt', 'w')
f2 = open('ucfTrainTestlist/test_file.txt', 'w')
f3 = open('ucfTrainTestlist/classInd.txt', 'w')
for action in action_list:
    video_list = os.listdir(video_path+action)
    prefixlist=[]
    labelnum+=1
    for video in video_list:
        prefix = video.split('.')[0]
        prefixlist.append(prefix)
        label = prefix.split('_')[0] 
    prefixlen=len(prefixlist)

    train = 0.8
    for i in range(int(prefixlen*0.8)):
        f1.write(prefixlist[i]+' '+str(labelnum)+'\n')
    for i in range(int(prefixlen*0.8),prefixlen):
        f2.write(prefixlist[i]+' '+str(labelnum)+'\n')
i=1
for action in action_list:
    f3.write(str(i)+' '+action+'\n')
    i+=1

