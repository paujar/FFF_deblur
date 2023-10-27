import cv2
import numpy as np
import glob
import shutil
import os
import statistics
import argparse
from tqdm import tqdm

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def move_blurry_images(min_focus_value, image_directory, blurry_directory, image_fm):
    # Get the images below the minimum focus value
    blurry_images = [img for fm, img in image_fm if fm < min_focus_value]
    
    for image_path in blurry_images:
        # Move the image
        shutil.move(image_path, blurry_directory + '/' + os.path.basename(image_path))

    print(f"Moved {len(blurry_images)} blurry images to {blurry_directory}.")

def main():
    parser = argparse.ArgumentParser(description='Move blurry images to a separate folder.')
    parser.add_argument('--input-folder', required=True, help='The directory containing your images.')
    parser.add_argument('--focus-filter', type=float, required=True, help='The minimum focus value.')

    args = parser.parse_args()

    image_directory = args.input_folder
    min_focus_value = args.focus_filter

    # Define blurry directory
    blurry_directory = image_directory + '/blurry'

    # Create the blurry directory if it doesn't exist
    os.makedirs(blurry_directory, exist_ok=True)

    # Calculate the variance of laplacian for all images and store it with the image path
    print("Calculating focus measure for all images...")
    images = glob.glob(image_directory + '/*.jpg') + glob.glob(image_directory + '/*.png') + glob.glob(image_directory + '/*.bmp')
    image_fm = []
    for img in tqdm(images):
        fm = variance_of_laplacian(cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY))
        image_fm.append((fm, img))

    # Sort the images based on the focus measure, from lowest (blurriest) to highest
    image_fm.sort()

    # Calculate the statistical measures
    fm_values = [fm for fm, img in image_fm]
    min_fm = min(fm_values)
    max_fm = max(fm_values)
    mean_fm = statistics.mean(fm_values)
    median_fm = statistics.median(fm_values)

    print(f"Statistics for focus measures:\nMinimum: {min_fm}\nMaximum: {max_fm}\nMean: {mean_fm}\nMedian: {median_fm}")

    # Move the blurriest images
    move_blurry_images(min_focus_value, image_directory, blurry_directory, image_fm)

if __name__ == "__main__":
    main()