import os
import json
from PIL import Image, ImageTk
import tkinter as tk
import shutil

def on_submit():
    global rating
    rating = float(rating_entry.get())
    assert 0 <= rating <= 1, "Invalid input, please enter a number between 0 and 1"
    save_rating()
    move_rated_image()
    show_next_image()

def move_rated_image():
    shutil.move(os.path.join(folder, image_files[i]), os.path.join(r"possible_dataset\rated", image_files[i]))

def save_rating():
    data = {"rating": rating}
    json_file = os.path.splitext(image_files[i])[0] + ".json"
    json_path = os.path.join(r"possible_dataset\rated", json_file)
    with open(json_path, "w") as f:
        json.dump(data, f)

def show_next_image():
    global i
    i += 1
    if i >= len(image_files):
        root.destroy()
        return
    # Checking if a json already exist isn't necessary because the pictures are in different folder.
    # However I decided to not remove it because it helps avoid multiple ratings for one picture if something gets messed up.
    while True:
        json_file = os.path.splitext(image_files[i])[0] + ".json"
        json_path = os.path.join(folder, json_file)
        if not os.path.exists(json_path):
            break
        i += 1
    image_path = os.path.join(folder, image_files[i])
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    label.config(image=image)
    label.image = image
    rating_entry.delete(0, tk.END)

folder = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\yet_to_be_rated"
image_files = os.listdir(folder)

root = tk.Tk()
root.title("Image Rating")

i = -1
image_path = os.path.join(folder, image_files[i])
image = Image.open(image_path)
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
label.pack()

rating_entry = tk.Entry(root)
rating_entry.pack()
rating_entry.bind("<Return>", lambda event: on_submit())


show_next_image()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()