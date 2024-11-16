# Face Blurring Project

This project detects faces in images and applies a Gaussian blur to each detected face. The modified images are saved in an output directory.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/drew22choi/FaceBlurringProject.git
cd blurFaces
```
### 2. Spin up a virtual env
```bash
python -m venv tf_env
source tf_env/bin/activate
```
### Install required libraries
```bash
pip install tensorflow
pip install tf-keras
pip install git+https://github.com/serengil/retinaface.git
```
### 3. Run script to blur images in a folder
By default, the output folder will be created at the same directory level if not specified
```bash
bash run_blur_faces.sh [path_to_original_images_folder] [path_to_modified_images_folder]
ex) bash run_blur_faces.sh /Users/drew.choi/PycharmProjects/blurFaces/input_images
```
