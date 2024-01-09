from PIL import Image
import os

# Set the target width and height for your images (e.g., 1080x1080)
target_width = 1080
target_height = 1080

# Set the directory where your images are located
image_dir = 'C:\Users\38641\OneDrive\Namizje\Development\Gorenc Detailing\gorenc-detailing\AvtoSlike\Škoda Karoq'

# Output directory for resized images
output_dir = 'C:\Users\38641\OneDrive\Namizje\Development\Gorenc Detailing\gorenc-detailing\AvtoSlike\Škoda Karoq\New folder'

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

            # Resize the image to the new dimensions
            img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # Create a new image with the target size and paste the resized image in the center
            new_img = Image.new('RGB', (target_width, target_height), (255, 255, 255))
            left = (target_width - new_width) // 2
            top = (target_height - new_height) // 2
            new_img.paste(img, (left, top))

            # Save the resized image to the output directory
            new_img.save(os.path.join(output_dir, filename))

print("Images resized to a common aspect ratio and saved to the output directory.")
