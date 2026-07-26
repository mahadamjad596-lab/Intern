import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("autoencoder.h5")

def denoise_image(image_path):
    # Read image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize to 28x28 (same size used during training)
    img = cv2.resize(img, (28, 28))

    # Normalize
    img = img.astype("float32") / 255.0

    # Reshape for the model
    img = img.reshape(1, 28, 28, 1)

    # Predict (denoise)
    result = model.predict(img)

    # Convert back to image
    result = result.reshape(28, 28)
    result = (result * 255).astype("uint8")

    return result

# Test the function
if __name__ == "__main__":
    output = denoise_image("test.jpg")  # Replace with your image name
    cv2.imwrite("denoised_output.jpg", output)
    print("Denoised image saved as denoised_output.jpg")