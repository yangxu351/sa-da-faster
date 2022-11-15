## Installation

### Requirements:
- PyTorch 1.0 from a nightly release. Installation instructions can be found in https://pytorch.org/get-started/locally/
- torchvision from master
- cocoapi
- yacs
- matplotlib
- GCC >= 4.9
- (optional) OpenCV for the webcam demo


### Option 1: Step-by-step installation

```bash
# first, make sure that your conda is setup properly with the right environment
# for that, check that `which conda`, `which pip` and `which python` points to the
# right path. From a clean conda env, this is what you need to do

conda create --name maskrcnn_benchmark
source activate maskrcnn_benchmark

# this installs the right pip and dependencies for the fresh python
conda install ipython

# maskrcnn_benchmark and coco api dependencies
pip install ninja yacs cython matplotlib

# follow PyTorch installation in https://pytorch.org/get-started/locally/
# we give the instructions for CUDA 9.0
conda install pytorch-nightly -c pytorch

# install torchvision
cd ~/github
git clone https://github.com/pytorch/vision.git
cd vision
python setup.py install

# install pycocotools
cd ~/github
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
python setup.py build_ext install

# install PyTorch Detection
# cd ~/github
# git clone https://github.com/facebookresearch/maskrcnn-benchmark.git
# cd maskrcnn-benchmark
# tag: yang changed
# 无需git clone maskrcnn-benchmark
# 因为clone 的项目已经有maskrcnn_benchmark了
直接 python setup.py build develop
# the following will install the lib with
# symbolic links, so that you can modify
# the files if you want and won't need to
# re-build it
# python setup.py build develop

# or if you are on macOS
# MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py build develop
```

### Option 2: Docker Image (Requires CUDA, Linux only)

Build image with defaults (`CUDA=9.0`, `CUDNN=7`):

    nvidia-docker build -t maskrcnn-benchmark docker/
    
Build image with other CUDA and CUDNN versions:

    nvidia-docker build -t maskrcnn-benchmark --build-arg CUDA=9.2 --build-arg CUDNN=7 docker/ 
    
Build and run image with built-in jupyter notebook(note that the password is used to log in jupyter notebook):

    nvidia-docker build -t maskrcnn-benchmark-jupyter docker/docker-jupyter/
    nvidia-docker run -td -p 8888:8888 -e PASSWORD=<password> -v <host-dir>:<container-dir> maskrcnn-benchmark-jupyter\



# 创建环境
conda create --name sada python=3.7
conda activate sada
# 切换cuda 版本，可由nvcc -V 查看版本
mkdir ~/anaconda3/envs/sada/etc/conda/activate.d
vim mkdir ~/anaconda3/envs/sada/etc/conda/activate.d/activate.sh

<!-- ORIGINAL_LD_LIBRARY_PATH=$LD_LIBRARY_PATH
ORIGINAL_PATH=$PATH 
export CUDA_PATH=/home/lab/yangDir/cuda-9.0
export LD_LIBRARY_PATH=$CUDA_PATH/lib64:$LD_LIBRARY_PATH
export PATH=$CUDA_PATH/bin:$PATH -->

mkdir ~/anaconda3/envs/sada/etc/conda/deactivate.d
vim mkdir ~/anaconda3/envs/sada/etc/conda/deactivate.d/deactivate.sh

<!-- export LD_LIBRARY_PATH=$ORIGINAL_LD_LIBRARY_PATH
export PATH=$ORIGINAL_PATH
unset CUDA_PATH
unset ORIGINAL_PATH
unset ORIGINAL_LD_LIBRARY_PATH  -->

# 配置环境
# 参考 https://pytorch.org/get-started/previous-versions/
conda install  pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch

# this installs the right pip and dependencies for the fresh python
conda install ipython [pip]

# maskrcnn_benchmark and coco api dependencies
pip install ninja yacs cython matplotlib tqdm opencv-python

# maskrcnn benchmark
cd ..
git clone https://github.com/yangxu351/maskrcnn-benchmark.git
cd maskrcnn-benchmark
# the following will install the lib with
# symbolic links, so that you can modify
# the files if you want and won't need to
# re-build it
python setup.py build develop