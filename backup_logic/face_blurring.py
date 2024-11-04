import os
import cv2
import face_recognition


def blur_faces(image_path):
    # Load the image using face_recognition
    image = face_recognition.load_image_file(image_path)
    # Find all face locations in the image
    face_locations = face_recognition.face_locations(image, model="cnn")

    # Convert the image to BGR color for OpenCV compatibility
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Iterate over all detected faces and apply a Gaussian blur to each face area
    for (top, right, bottom, left) in face_locations:
        # Extract the face region
        face = image[top:bottom, left:right]
        # Apply a blur effect on the face region
        blurred_face = cv2.GaussianBlur(face, (99, 99), 30)  # Adjust blur strength as needed
        # Replace the original face region with the blurred version
        image[top:bottom, left:right] = blurred_face

    # Return the image with all faces blurred
    return image


def process_images(input_folder='input_images', output_folder='output_images'):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an image (you can add more image extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Blur faces in the image
            blurred_image = blur_faces(file_path)

            # Save the modified image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, blurred_image)
            print(f"Processed and saved: {output_path}")

# Example usage:
# Set input_folder and output_folder paths as needed
# process_images('input_images', 'output_images')
