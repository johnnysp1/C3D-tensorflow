## 90% of code come from https://github.com/lianggyu/C3D-Action-Recognition
## C3D-Action-Recognition
Train the C3D network with UCF-101(as an example) or other dataset. Video or gif can be supported as a training file. Video streams or image frames can be used as input for detection.

## Environment
* python == 3.6
* opencv-python == 4.5.1.48
* keras == 2.0.8
* tensorflow-gpu == 1.3
* pillow == 8.1.2
* matplotlib == 3.3.4
* h5py : $ pip install h5py==2.10 -i https://pypi.tuna.tsinghua.edu.cn/simple/
* cuda 8
* cudnn 6
## Train your own data
* Place the videos in the `datasets/ucf-101`, the videos must be named as `category_name.avi`, there are already three categories in the `datasets/ucf-101` as examples.

* If you are using UCF-101 dataset, run `rename.py` after you place videos in `datasets/ucf-101`.

* Run the `video2list.py` to get the label for training (`train_file.txt`), the label for testing (`test_file.txt`), and the record category (`classInd.txt`), which are all placed in the `/ucfTrainTestlist`.

* Run `video2img.py` and save it in the `datasets/ucfimgs`. Currently gif and video formats are supported.

* Run `make_label_txt.py` and generate `train_list.txt` and `test_list.txt`.

* Modify `model.py`, such as lines 7~9.

* Modify `train_c3d.py`, such as lines 158~164. Run `train_c3d.py`.

* After these, run `train_c3d.py` to train your dataset.
## Demo
* Modify `config.txt`<br>
  classInd_path : the file path of the record category<br>
  lr : learning rate (default 0.005)<br>
  momentum : Momentum (default 0.9)<br>
  weights_path : path to the trained model<br>
  
  Image mode:<br>
  image_read : the path to the image read<br>
  image_write : the path written by the image<br>
  
  video_image: select input mode<br>
  video: the mode of video input<br>
  image: the mode of image input<br>
  <br>
* Modify `video_demo.py`<br>
  If you want to apply it to the video stream, you must first modify the dictionary(video_stream).<br>
  video_stream[key].[0] : This is an array that records 16 video frames as input to the model.<br>
  video_stream[key].[1] : the path to the data.<br>
  video_stream[key].[2] : the path of the model.<br>
  <br>
 * Run `video_demo.py`<br>
 Identification of UCF-101
 <img src="https://github.com/johnnysp1/C3D-tensorflow/blob/master/results/Archery.png"/>     

 
