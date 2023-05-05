# //////////////////////////////////////////
# AUTOSIG with PNG watermark
# v 1.1
# --------------------------------------
# GAIO.AI 
# Michael Gaio - MichaelGaio.com
# Mythic Systems - MythicSystems.com
# //////////////////////////////////////////

from PIL import Image, ImageDraw, ImageFont
import os

# Parameters
series_title = "Gamma-Ray-Girl"
watermark_path = '_watermarks/GAIO.AI-text-watermark.png'
watermark_size = (60, 17)
watermark_transparency = 0.2
x_adjustment = -5
y_adjustment = -5
max_width = 600
max_height = None

# Add watermark to image
def add_watermark(image_path, watermark_path, size, transparency, x_adjustment, y_adjustment, series_title, file_number):
    try:
        # Open the image and watermark
        image = Image.open(image_path).convert('RGBA')
        watermark = Image.open(watermark_path).convert('RGBA')

        # Calculate the new x and y adjustments based on the ratio of the original image size to the resized image size
        x_ratio = image.size[0] / size[0]
        y_ratio = image.size[1] / size[1]
        new_x_adjustment = int(x_adjustment / x_ratio)
        new_y_adjustment = int(y_adjustment / y_ratio)

        # Resize the image to the desired size
        image = image.resize(size)

        # Resize the watermark to the desired size
        #watermark_width = int(watermark_size[0] / x_ratio)
        #watermark_height = int(watermark_size[1] / y_ratio)
        #watermark_size_resized = (watermark_width, watermark_height)
        #watermark = watermark.resize(watermark_size_resized)

        # Resize the watermark to the desired size
        watermark = watermark.resize(watermark_size)

        # Add transparency to the watermark
        # print(f"Watermark mode: {watermark.mode}")
        # watermark = watermark.convert('RGBA')
        alpha = int(255 * transparency)
        watermark.putalpha(alpha)

        # Calculate the position of the watermark based on adjustments
        watermark_position = (size[0] - watermark.size[0] + x_adjustment, size[1] - watermark.size[1] + y_adjustment)

        # Blend the watermark with the image
        image.alpha_composite(watermark, watermark_position)

        # Convert the image to RGB mode if necessary
        if image.mode != "RGB":
            image = image.convert('RGB')

        # Save the adjusted image with the "GAIO_" prefix and series title and number
        file_number_str = str(file_number).zfill(3) # pad with leading zeros
        output_filename = f"GAIO--{series_title}-{file_number_str}{os.path.splitext(image_path)[1].lower()}"
        output_path = os.path.join(output_folder, output_filename)

        # Save the output image
        image.save(output_path)
        print(f"Processed file: {image_path}")
        print(f"Output file: {output_path}")
    except Exception as e:
        print(f"Error processing file: {image_path}, error: {e}")

# Input and output folders
input_folder = '_input'
output_folder = '_output'

# Resize an image proportionally with one or more variables
def resize_image_proportionally(image_path, max_width=None, max_height=None):
    image = Image.open(image_path)
    width, height = image.size
    if max_width and max_height:
        # Resize based on whichever dimension requires the larger resize
        width_ratio = max_width / float(width)
        height_ratio = max_height / float(height)
        ratio = min(width_ratio, height_ratio)
    elif max_width:
        # Resize based on width
        ratio = max_width / float(width)
    elif max_height:
        # Resize based on height
        ratio = max_height / float(height)
    else:
        # No resize necessary
        return (width, height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    resized_size = (new_width, new_height)
    print(f"Resized image size: {resized_size}")
    return resized_size


# Get list of input files sorted alphabetically
input_files = sorted([entry for entry in os.scandir(input_folder) if entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png'))], key=lambda x: x.name.lower())

# Initialize file number counter
file_number = 1

# Loop through all images in input folder
for entry in input_files:
    filename = entry.name
    print(f">>> Processing file: {filename}")
    image_path = os.path.join(input_folder, filename)

    # Resize image based on both max_width and max_height
    size = resize_image_proportionally(image_path, max_width, max_height)

    # Add watermark to image
    add_watermark(image_path, watermark_path, size, watermark_transparency, x_adjustment, y_adjustment, series_title, file_number)

    # Increment file number counter
    file_number += 1

