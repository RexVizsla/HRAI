from PIL import Image
import os

def downscale_image(image_path, target_size=(2000, 2000)):
    # Open the image
    with Image.open(image_path) as im:
        # Check if the image is smaller than the target size
        if im.size[0] > target_size[0] or im.size[1] > target_size[1]:
            # Downscale the image to max 2000p
            width, height = im.size
            ratio = max(2000/width, 2000/height)
            new_size = (int(width*ratio), int(height*ratio))
            im = im.resize(new_size, resample=Image.LANCZOS)
            # Save the downscaled image
            filename, file_extension = os.path.splitext(os.path.basename(image_path))
            im.save(os.path.join(image_path_downscaled,f"{filename}_downscaled.jpeg"))
            print("Downscaled image with name '" + os.path.basename(im) + "' to " + str(new_size))

image_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated"
image_path_downscaled = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated\downscaled"

for image in os.listdir(image_path):
    try:
        downscale_image(os.path.join(image_path,image))
    except UnidentfiedImageError:
        print("File with name '" + os.path.basename(im) + "' cant be downscaled because its not an image")