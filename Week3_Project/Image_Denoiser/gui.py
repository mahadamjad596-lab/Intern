import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("autoencoder.h5")

original_image = None
denoised_image = None


def show_image(img, label):
    image = Image.fromarray(img)
    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo


def upload_image():
    global original_image

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )

    if not file_path:
        return

    original_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if original_image is None:
        messagebox.showerror("Error", "Could not open image.")
        return

    show_image(original_image, original_label)


def denoise():
    global denoised_image

    if original_image is None:
        messagebox.showwarning("Warning", "Upload an image first.")
        return

    img = cv2.resize(original_image, (28, 28))
    img = img.astype("float32") / 255.0
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img, verbose=0)

    denoised_image = prediction.reshape(28, 28)
    denoised_image = (denoised_image * 255).astype(np.uint8)

    show_image(denoised_image, denoised_label)


def save_image():
    if denoised_image is None:
        messagebox.showwarning("Warning", "No denoised image to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )

    if file_path:
        cv2.imwrite(file_path, denoised_image)
        messagebox.showinfo("Success", "Image saved successfully.")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Image Denoiser using TensorFlow")
root.geometry("900x600")
root.configure(bg="white")

title = tk.Label(
    root,
    text="Image Denoiser using TensorFlow",
    font=("Arial", 20, "bold"),
    bg="white"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

original_label = tk.Label(
    frame,
    text="Original Image",
    width=35,
    height=15,
    bg="lightgray",
    relief="solid"
)
original_label.grid(row=0, column=0, padx=20)

denoised_label = tk.Label(
    frame,
    text="Denoised Image",
    width=35,
    height=15,
    bg="lightgray",
    relief="solid"
)
denoised_label.grid(row=0, column=1, padx=20)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Upload Image",
    width=18,
    command=upload_image
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Denoise Image",
    width=18,
    command=denoise
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Save Image",
    width=18,
    command=save_image
).grid(row=0, column=2, padx=10)

root.mainloop()