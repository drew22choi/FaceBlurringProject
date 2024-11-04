# Face Blurring Project

This project detects faces in images and applies a Gaussian blur to each detected face. The modified images are saved in an output directory.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/drew22choi/FaceBlurringProject.git
cd blurFaces
```
### 2. Install required libraris
```bash
pip install -r requirements.txt
```
### 3. Run script to blur images in a folder
By default, the output folder will be created at the same directory level if not specified
```bash
bash run_blur_faces.sh [path_to_original_images_folder] [path_to_modified_images_folder]
ex) bash run_blur_faces.sh /Users/drew.choi/PycharmProjects/blurFaces/input_images
```
