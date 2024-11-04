import os
import cv2
from retinaface import RetinaFace


def blur_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Detect faces using RetinaFace
    detections = RetinaFace.detect_faces(image)

    if isinstance(detections, dict):  # Check if detections were found
        for key, face in detections.items():
            # Extract the bounding box for each detected face
            x1, y1, x2, y2 = face['facial_area']

            # Crop the face region from the image
            face_region = image[y1:y2, x1:x2]

            # Apply a Gaussian blur to the face region
            blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

            # Replace the original face region with the blurred version
            image[y1:y2, x1:x2] = blurred_face

    # Return the image with faces blurred
    return image


def process_images(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an image (supports common formats)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Blur faces in the image
            blurred_image = blur_faces(file_path)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, blurred_image)
            print(f"Processed and saved: {output_path}")
