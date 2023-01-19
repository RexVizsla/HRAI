import os
import shutil

# Folder to scan
src_folder = r'C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\yet_to_be_rated'
# Folder to move non-image files to
dst_folder = r'C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\invalid_file_format'

# Iterate through all files in the source folder
for file_name in os.listdir(src_folder):
    # Get the file extension
    extension = os.path.splitext(file_name)[1]
    # Check if the file extension can be opened by PIL
    if extension.lower() not in ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'):
        # Construct the full path of the file to move
        src_path = os.path.join(src_folder, file_name)
        dst_path = os.path.join(dst_folder, file_name)
        # Move the file to the destination folder
        shutil.move(src_path, dst_path)
