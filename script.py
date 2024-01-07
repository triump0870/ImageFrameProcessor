import pandas as pd

from app.image_processing import resize_image
from app.models import save_to_database


def load_image():
    df = pd.read_csv('data/img.csv')
    for index, row in df.iterrows():
        depth = row['depth']
        pixel_values = row[1:]  # Assuming pixel values start from the second column
        resized_pixel_data = resize_image(pixel_values)
        save_to_database(depth, resized_pixel_data)
        print('Processing and saving complete')


if __name__ == "__main__":
    load_image()
