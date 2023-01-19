from PIL import Image

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
            im.save(image_path)

# add folder interating here
downscale_image('image.jpg')