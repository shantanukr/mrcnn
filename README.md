# mrcnn
training of mask rcnn on self created dataset using python and tensorflow

Basic system reqirement
1. windows os
2. nvidia gpu
3. installation of CUDA
4. installation od CUDAnn
5. Anaconda
6. python 3

step 1 clone the above repository and extract it into your local system and open cmd in that directory

step 2 download the pre trained coco weight from the given link below.
https://github.com/matterport/Mask_RCNN/releases
and select mask_rcnn_coco.h5 from mask rcnn 2.0 version and place it in the project directory.

step 3 creation of virtual conda enviornment
open cmd and run the command
conda create -n myenv

step 4 enter into the virtual enviornment
conda activate myenv
  
step 5 install all the dependencies by using following command
pip install tensorflow-gpu==1.13.1

pip install q keras==2.1.0

pip install -r requirements.txt

Run setup from the repository root directory

python setup.py install

* if you donot have jupyter notebook install in your enviornment use this command
pip install notebook

step 6 open jupyter notebook using command
jupyter notebook

and navigate to the mines.ipynb file and press shift + enter to execute that a code block.






