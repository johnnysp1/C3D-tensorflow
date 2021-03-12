import cv2
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

video_path = '/c3d2/C3D-Action-Recognition/datasets/ucf-101/'
labelnum=-1
labellist=[]
action_list = os.listdir(video_path)
f1 = open('/c3d2/C3D-Action-Recognition/ucfTrainTestlist/train_file.txt', 'w')
f2 = open('/c3d2/C3D-Action-Recognition/ucfTrainTestlist/test_file.txt', 'w')
f3 = open('/c3d2/C3D-Action-Recognition/ucfTrainTestlist/classInd.txt', 'w')
for action in action_list:
    video_list = os.listdir(video_path+action)
    prefixlist=[]
    labelnum+=1
    for video in video_list:
        prefix = video.split('.')[0]
        prefixlist.append(prefix)
        label = prefix.split('_')[0] 
        """
        if label not in labellist:
            labellist.append(label)
            labelnum+=1
        #print(prefix)
        f1.write(prefix+' '+str(labelnum)+'\n')
        """
    prefixlen=len(prefixlist)
    #print(prefixlen)
    train = 0.8
    for i in range(int(prefixlen*0.8)):
        f1.write(prefixlist[i]+' '+str(labelnum)+'\n')
    for i in range(int(prefixlen*0.8),prefixlen):
        f2.write(prefixlist[i]+' '+str(labelnum)+'\n')
i=1
for action in action_list:
    f3.write(str(i)+' '+action+'\n')
    i+=1
"""
        if not os.path.exists(save_path+action+'/'+prefix):
            os.mkdir(save_path+action+'/'+prefix)
        save_name = save_path + action + '/' + prefix + '/'
        #save_name = save_path + prefix + '/'
        video_name = video_path+action+'/'+video
        #print(video_name)
        name = video_name.split('.')[1]
        #print(name)
"""
