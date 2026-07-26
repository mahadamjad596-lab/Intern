<div align="center">

# 🖼️ Image Denoiser (v2)

### AI-Powered Image Noise Removal using TensorFlow & Tkinter

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange.svg)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-green.svg)]()
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-red.svg)]()
[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)]()

*A desktop application that removes noise from images using a Deep Learning Autoencoder with an intuitive graphical user interface.*

</div>

---

# 📖 Overview

**Image Denoiser (v2)** is an Artificial Intelligence project that demonstrates how Deep Learning can restore noisy images.

The application is powered by a **Convolutional Autoencoder** built with TensorFlow/Keras and provides an easy-to-use desktop interface developed using Tkinter.

Users can upload an image, remove noise using the trained AI model, preview the results, and save the enhanced image.

---

# ✨ Features

✔ Upload Images

✔ AI-Based Image Denoising

✔ TensorFlow Autoencoder Model

✔ User-Friendly GUI

✔ Real-Time Image Preview

✔ Save Denoised Images

✔ Clean & Organized Source Code

✔ Beginner Friendly

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🤖 TensorFlow / Keras | Deep Learning |
| 📷 OpenCV | Image Processing |
| 🖼 Pillow | Image Display |
| 🔢 NumPy | Numerical Computing |
| 🖥 Tkinter | Desktop GUI |

---

# 📂 Project Structure

```
Image_Denoiser/

│── gui.py
│── train_model.py
│── denoise.py
│── autoencoder.h5
│── requirements.txt
│── README.md

├── dataset/
│     ├── train/
│     └── test/

├── output/

└── images/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Image_Denoiser.git
```

Move into the project

```bash
cd Image_Denoiser
```

Install required libraries

```bash
pip install tensorflow opencv-python pillow numpy
```

---

# 🚀 Running the Project

### 1️⃣ Train the AI Model

```bash
python train_model.py
```

---

### 2️⃣ Launch the GUI

```bash
python gui.py
```

---

# 🖥 Application Workflow

```
User
   │
   ▼
Upload Image
   │
   ▼
Preprocessing
   │
   ▼
TensorFlow Autoencoder
   │
   ▼
Image Denoising
   │
   ▼
Display Result
   │
   ▼
Save Image
```

---

# 🧠 Deep Learning Architecture

The application uses a **Convolutional Autoencoder** consisting of:

### Encoder

- Conv2D
- ReLU Activation
- MaxPooling
- Feature Compression

### Decoder

- Conv2D
- UpSampling
- Reconstruction Layer
- Sigmoid Activation

The network learns to reconstruct clean images from noisy inputs.

---

# 📸 Application Features

- 📂 Upload noisy image
- 🧠 AI-based denoising
- 🖼 Display original image
- ✨ Display denoised image
- 💾 Save processed image

---

# 📈 Future Improvements

- ✅ Color Image Denoising
- ✅ Batch Processing
- ✅ Drag & Drop Images
- ✅ Better GUI Design
- ✅ GPU Acceleration
- ✅ High Resolution Support
- ✅ Multiple AI Models
- ✅ Image Quality Metrics

---

# 🎯 Learning Outcomes

This project demonstrates concepts of:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Autoencoders
- Image Processing
- Computer Vision
- Python GUI Development
- TensorFlow
- OpenCV

---

# 👨‍💻 Author

## Mahad Amjad

**Course:** Artificial Intelligence & Machine Learning

**Project:** Image Denoiser (v2)

**Language:** Python

---

# 🤝 Contribution

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository and submit a pull request.

---

# ⭐ Support

If you like this project, don't forget to **Star ⭐ the repository**.

---

# 📄 License

This project was developed for **educational and academic purposes** as part of an Artificial Intelligence & Machine Learning coursework project.

---

<div align="center">

## 💙 Thank You for Visiting

Made with ❤️ using Python, TensorFlow & OpenCV

</div>
