from PIL import Image, ImageOps
import os

# Set the desired width and height for your images
target_width = 400
target_height = 267  # Choose the maximum dimensions

# Set the directory where your images are located
image_dir = r'C:\Users\38641\OneDrive\Namizje\Development\Gorenc Detailing\gorenc-detailing\Slike'

# Output directory for resized images
output_dir = r'C:\Users\38641\OneDrive\Namizje\Development\Gorenc Detailing\gorenc-detailing\Slike\resized'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through the files in the input directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Open the image file
        with Image.open(os.path.join(image_dir, filename)) as img:
            # Calculate new dimensions while maintaining the aspect ratio
            width, height = img.size
            aspect_ratio = width / height

            if aspect_ratio > 1:
                new_width = target_width
                new_height = int(target_width / aspect_ratio)
            else:
                new_width = int(target_height * aspect_ratio)
                new_height = target_height

            # Calculate the padding to create a border
            padding_width = (target_width - new_width) // 2
            padding_height = (target_height - new_height) // 2

            # Add a border with a white background
            bordered_img = ImageOps.expand(img, (padding_width, padding_height, padding_width, padding_height), fill="white")

            # Save the resized and bordered image to the output directory
            bordered_img.save(os.path.join(output_dir, filename))

print("Images resized and bordered to the specified dimensions and saved to the output directory.")
