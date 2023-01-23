import os
from PIL import Image

def calculate_average(folder_path):
    total_x_resolution = 0
    total_y_resolution = 0
    total_aspect = 0
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                count += 1
                file_path = os.path.join(root, file)
                with Image.open(file_path) as img:
                    width, height = img.size
                    total_x_resolution += width
                    total_y_resolution += height
                    total_aspect += (width / height)
    average_x_resolution = total_x_resolution / count
    average_y_resolution = total_y_resolution / count
    average_aspect = total_aspect / count
    return average_x_resolution, average_y_resolution, average_aspect, count
    
def count_files(unrated_folder_path, rated_folder_path):
    unrated_files = len(os.listdir(unrated_folder_path))
    rated_files = len(os.listdir(rated_folder_path))//2
    return rated_files, unrated_files

folder_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset"
rated_folder_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated"
unrated_folder_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\yet_to_be_rated"
average_x_resolution, average_y_resolution, average_aspect, count = calculate_average(folder_path)
rated_files, unrated_files = count_files(rated_folder_path, unrated_folder_path)
print("Folder contains a total of", count,"images. There are", rated_files,"rated and", unrated_files,"unrated images.")
print("Average resolutions:")
print("Average X resolution:", average_x_resolution)
print("Average Y resolution:", average_y_resolution)
print("Average aspect ratio:", average_aspect)
