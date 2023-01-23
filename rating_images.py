import os
import json
from PIL import Image, ImageTk
import tkinter as tk
import shutil

global json_path
json_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated"

def on_submit():
    global rating
    rating = int(rating_entry.get())
    assert 0 <= rating <= 100, "Invalid input, please enter a number between 0 and 100"
    rating = float(rating*0.01)
    save_rating()
    move_rated_image()
    show_next_image()

def move_rated_image():
    shutil.move(os.path.join(folder, image_files[i]), os.path.join(r"possible_dataset\rated", image_files[i]))

def save_rating():
    json_file = os.path.splitext(image_files[i])[0] + ".json"
    json_path = os.path.join(r"possible_dataset\rated", json_file)
    with open(json_path, "w") as f:
        json.dump({"rating": rating}, f)

def show_next_image():
    global i
    while True:
        i += 1
        json_file = os.path.splitext(image_files[i])[0] + ".json"
        json_path = os.path.join(r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated", json_file)
        if not os.path.exists(json_path):
            break
    if i >= len(image_files):
        root.destroy()
        return
    image_path = os.path.join(folder, image_files[i])
    image = Image.open(image_path)
    width, height = image.size
    ratio = min(2000/width, 1200/height)
    new_size = (int(width*ratio), int(height*ratio))
    image = image.resize(new_size, Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    label.config(image=image)
    label.image = image
    rating_entry.delete(0, tk.END)


folder = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\yet_to_be_rated"
image_files = os.listdir(folder)

root = tk.Tk()
root.title("Image Rating")

i = -1

label = tk.Label(root)
label.pack()

rating_entry = tk.Entry(root)
rating_entry.pack()
rating_entry.bind("<Return>", lambda event: on_submit())

show_next_image()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()