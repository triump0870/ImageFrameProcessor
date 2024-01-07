from app.image_processing import visualize_frames, generate_frames
from app.models import ImageData
from app import app
import csv
import numpy as np
import matplotlib.pyplot as plt


def plot():
    depth_min = 9000
    depth_max = 9001
    with app.app_context():
        image_data = ImageData.query.filter(ImageData.depth.between(depth_min, depth_max)).all()
    frames = []
    for image in image_data:
        frames.append(generate_frames(image))

    visualize_frames(frames)


def plot_image_from_csv():
    # Load pixel values from the CSV file
    csv_file_path = "data/img.csv"  # Replace with your CSV file path
    pixel_values = []

    with open(csv_file_path, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Skip the header row if present
        for row in csv_reader:
            pixel_values.append([float(value) for value in row])

    # Convert the pixel values to a NumPy array
    image_array = np.array(pixel_values)

    # Plot the image using Matplotlib
    plt.imshow(image_array, cmap="gray")  # Use "gray" colormap for grayscale images
    plt.title("Image Plot")
    plt.show()


if __name__ == "__main__":
    plot_image_from_csv()
    plot()
