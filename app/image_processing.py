# app/image_processing.py
from PIL import Image


def resize_image(pixel_values):
    pixel_matrix = np.array(pixel_values).reshape((1, 200)).astype('uint8')
    img = Image.fromarray(pixel_matrix)
    resized_img = img.resize((150, img.height))
    resized_pixel_values = np.array(resized_img).flatten()
    return resized_pixel_values.tobytes()


# Assuming you have a function to get image data
def get_image_data():
    # Replace this with your actual logic to fetch image data
    depth_data = np.genfromtxt('img.csv', delimiter=',', skip_header=1)
    return depth_data


# Function to generate frames with a custom color map
def generate_frames(image):
    # Apply your custom color map to pixel_values
    # Replace this with your actual custom color map logic
    colored_frames = apply_custom_color_map(image.pixel_data)
    return colored_frames


def apply_custom_color_map(pixel_values):
    # Replace this with your actual custom color map logic
    # This is a placeholder example using a simple colormap
    colormap = plt.get_cmap('viridis')
    # Convert byte data to NumPy array
    numeric_array = np.frombuffer(pixel_values, dtype=np.uint8)
    # Normalize pixel values to the range [0, 1] if needed
    # numeric_array = numeric_array / 255.0
    colored_frames = colormap(numeric_array)
    return colored_frames.tolist()


import matplotlib.pyplot as plt
import numpy as np


def visualize_frames(frames):
    num_frames = len(frames)

    # Set up a grid for subplots
    rows = int(np.ceil(num_frames / 5))  # 5 frames per row (adjust as needed)
    cols = min(num_frames, 5)

    plt.figure(figsize=(15, 3 * rows))  # Adjust the figure size as needed

    for i, frame in enumerate(frames):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(frame)
        plt.axis('off')

    plt.show()
