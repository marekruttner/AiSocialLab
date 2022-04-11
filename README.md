# AiSocialLab
**install**
- Clone git repository
- Install requirements.txt with pip install -r requirements.txt
- Run main.py
- Stop by pressing q on keyboard

**hardware requirements**
- Minimum for running with minimal lags RTX 3060 with CUDA enabled

**training on full COCO dataset**
- uncomment lines from 866 to 900
- chachage model_dir from data to retinanet in line 907
**v1**
- Stable 
- Running detections on video stream from camera 
- Using RetinaNet and part of COCO dataset
- Can be trained on full COCO dataset 

**v1-b1**
- Opening video stream from camera with cv2 and running detections on each frame 
- Not working 
- Problem with tf: biases on input 

**v1-a1**
- Sequence of taking photos and opening it in matplotlib
- Slow, but working

