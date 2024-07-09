import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_tonal_ranges(histogram, total_pixels):
    blacks = sum(histogram[:51]) / total_pixels * 100
    shadows = sum(histogram[51:102]) / total_pixels * 100
    midtones = sum(histogram[102:153]) / total_pixels * 100
    highlights = sum(histogram[153:204]) / total_pixels * 100
    whites = sum(histogram[204:]) / total_pixels * 100
    return blacks, shadows, midtones, highlights, whites

def process_image(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Grayscale histogram
    grayscale_histogram = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256]).flatten()
    total_pixels = np.sum(grayscale_histogram)
    grayscale_tonals = calculate_tonal_ranges(grayscale_histogram, total_pixels)
    
    # RGB histograms
    rgb_tonals = []
    for i in range(3):  # B, G, R channels
        channel_histogram = cv2.calcHist([image], [i], None, [256], [0, 256]).flatten()
        total_pixels = np.sum(channel_histogram)
        tonals = calculate_tonal_ranges(channel_histogram, total_pixels)
        rgb_tonals.append(tonals)
    
    return grayscale_tonals, rgb_tonals

def display_histogram(image_path):
    image = cv2.imread(image_path)
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 6))
    
    for i, color in enumerate(colors):
        channel_histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(channel_histogram, color=color)
    
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale_histogram = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])
    plt.plot(grayscale_histogram, color='k', linestyle='dotted')
    
    plt.title('Histograms for RGB Channels and Grayscale')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()