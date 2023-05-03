# //////////////////////////////////////////
# AUTOSIG with PNG watermark
# --------------------------------------
# GAIO.AI 
# Michael Gaio - MichaelGaio.com
# Mythic Systems - MythicSystems.com
# //////////////////////////////////////////

from PIL import Image, ImageDraw, ImageFont
import os

# Add watermark to image
def add_watermark(image_path, watermark_path, size, transparency, x_adjustment, y_adjustment, series_title, file_number):
    try:
        # Open the image and watermark
        image = Image.open(image_path).convert('RGBA')
        watermark = Image.open(watermark_path).convert('RGBA')

        # Calculate the position of the watermark based on adjustments
        watermark_position = (image.size[0] - watermark.size[0] + x_adjustment, image.size[1] - watermark.size[1] + y_adjustment)

        # Resize the watermark to the desired size
        watermark = watermark.resize(size)

        # Add transparency to the watermark
        print(f"Watermark mode: {watermark.mode}")
        # watermark = watermark.convert('RGBA')
        alpha = int(255 * transparency)
        watermark.putalpha(alpha)

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

# Parameters
series_title = "Gamma-Ray-Girl"
watermark_path = '_watermarks/GAIO.AI-text-watermark.png'
#watermark_size = (60, 76) # GAIO.AI-watermark (230, 290)
watermark_size = (60, 17) # GAIO.AI-text-watermark (230, 60)
watermark_transparency = 0.2
x_adjustment = 230
y_adjustment = 60

# Input and output folders
input_folder = '_input'
output_folder = '_output'

# Get list of input files sorted alphabetically
input_files = sorted([entry for entry in os.scandir(input_folder) if entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png'))], key=lambda x: x.name.lower())

# Initialize file number counter
file_number = 1

# Loop through all images in input folder
for entry in input_files:
    filename = entry.name

    print(f">>> Processing file: {filename}")

    image_path = os.path.join(input_folder, filename)

    # Add watermark to image
    add_watermark(image_path, watermark_path, watermark_size, watermark_transparency, x_adjustment, y_adjustment, series_title, file_number)

    # increment file number counter
    file_number += 1
