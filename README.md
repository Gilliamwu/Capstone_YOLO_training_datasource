# Capstone_YOLO_training_datasource
## Introduction
This is the self-labeled data for Aeolus Computer vision backend.
There are three parts:
* images: containing all the images from three data sources
* labels: self-labelling of the cracks on these images
* test.txt: for training of model
* train.txt: for training of model
* yolov3-obj_3100.weights (in dropbox): weight of crack detection after training 3100 epoches
* yolov3-obj_1300.weights (in dropbox): weight of crack detection after training 1300 epoches


## How to use it:
### If you just want to use it for detection:
Get capstone server code from https://github.com/Gilliamwu/Capstone_DB_code

Put the  yolov3-obj_3100.weights under backup folder. If backup folder doesn't exist, create one.

Remember to edit settings.py and update the weight name

run the following command in bash:
```
make
./darknet detector test cfg/obj.data cfg/yolov3-obj.cfg backup/yolov3-obj_1300.weights data/obj/904.JPEG(image file location)
```

### If you have new images, and further train the model
The training of the whole model is based on this post: https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/

Get the modified darknet version from https://github.com/Gilliamwu/darknet

Put the weight file you want to start under backup folder.

copy images and labesl under data/obj

copy train.txt and test.txt

For setup, Make sure cuda is installed, or you can edit Makefile based on your setup. Current requirement:
* Linux GCC>=4.9
* GPU with CC >= 3.0:
* cuDNN v5-v7
* CUDA >= 7.5

Follow instructionss of darknet, run following commands (assume we start from weight 3100)
```
./darknet detector train cfg/obj.data cfg/yolov3-obj.cfg backup/yolov3-obj_3100.weights 
```

Then if Database+Flask backend need the newest weight, repeat "If you just want to use it for detection", but change the weight file name by the latest weight


## How to add your own data
### launch BBox training tool to do the labelling
Find the labelling tool from here: https://github.com/puzzledqs/BBox-Label-Tool

Remember to translate all images to JPEG. Put them under Images folder with number, and in the main window, key in the number and label

### translate BBox label to YOLO label
Use labelling_tool/convert.py, to convert the crack data to YOLO data

### generate train.txt and test.txt
Use labelling_tool/generate_train_test_list.py to generate two files, separating data to train and test.

Then repeat the steps in "If you have new images, and further train the model" section

## related github:
darknet: https://github.com/Gilliamwu/darknet

capstone server code: https://github.com/Gilliamwu/Capstone_DB_code

## Special notes
### When should I stop my training?
As the original darknet repository mentioned, when maybe after 8000 iterations, average loss is not dropping anymore, you could probably stop.

## Data sources:
Crack forest: Amhaz, R., Chambon, S., Idier, J., & Baltazart, V. (2014). A new minimal path selection algorithm for automatic crack detection on pavement images. 2014 IEEE International Conference on Image Processing (ICIP). doi:10.1109/icip.2014.7025158

Crack detection database: Yong Shi, Limeng Cui, Zhiquan Qi, Fan Meng, and Zhensong Chen.  Automatic road crack detection using random structured forests. IEEE Transactions on Intelligent Transportation Systems, 17(12):3434–3445, 2016
