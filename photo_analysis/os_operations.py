import os
import pandas as pd

def process_directory(directory, process_image_function):
    data = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
            image_path = os.path.join(directory, filename)
            grayscale_tonals, rgb_tonals = process_image_function(image_path)
            data.append({
                'Filename': filename,
                'Grayscale Blacks (%)': grayscale_tonals[0],
                'Grayscale Shadows (%)': grayscale_tonals[1],
                'Grayscale Midtones (%)': grayscale_tonals[2],
                'Grayscale Highlights (%)': grayscale_tonals[3],
                'Grayscale Whites (%)': grayscale_tonals[4],
                'Red Blacks (%)': rgb_tonals[2][0],
                'Red Shadows (%)': rgb_tonals[2][1],
                'Red Midtones (%)': rgb_tonals[2][2],
                'Red Highlights (%)': rgb_tonals[2][3],
                'Red Whites (%)': rgb_tonals[2][4],
                'Green Blacks (%)': rgb_tonals[1][0],
                'Green Shadows (%)': rgb_tonals[1][1],
                'Green Midtones (%)': rgb_tonals[1][2],
                'Green Highlights (%)': rgb_tonals[1][3],
                'Green Whites (%)': rgb_tonals[1][4],
                'Blue Blacks (%)': rgb_tonals[0][0],
                'Blue Shadows (%)': rgb_tonals[0][1],
                'Blue Midtones (%)': rgb_tonals[0][2],
                'Blue Highlights (%)': rgb_tonals[0][3],
                'Blue Whites (%)': rgb_tonals[0][4]
            })
    return data

def write_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)