# AutoSIG
Automatically sign images with a png graphic watermark


## Install and run

Here are the steps to install and run the script:

1. Install Python: First, you need to install Python on your computer. You can download and install Python from the official website: https://www.python.org/downloads/

2. Install Pillow library: The script requires the Pillow library to work with images. You can install the library by running the following command in your terminal or command prompt: `pip install Pillow`

3. Prepare input and watermark images: Place your input images in a folder named `_input` and your watermark image in a folder named `_watermarks`. Make sure your watermark image has a transparent background and is in PNG format.

4. Update parameters: Open the script in a text editor and update the following parameters as needed:

   - `series_title`: The title of the series that the images belong to.
   - `watermark_path`: The path to the watermark image file.
   - `watermark_size`: The size of the watermark image.
   - `watermark_transparency`: The transparency level of the watermark image.
   - `x_adjustment`: The horizontal adjustment for the watermark position.
   - `y_adjustment`: The vertical adjustment for the watermark position.
   - `max_width`: The maximum width adjustment for the image.
   - `max_height`: The height width adjustment for the image.

5. Run the script: Open your terminal or command prompt, navigate to the directory where the script is located, and run the script by running the following command: `python3 autosig.py`

6. Check the output: The script will save the processed images with the watermark in a folder named `_output`. Check this folder to see the results.


### Features:

- Adds a PNG watermark to images in a specified folder
- Watermark size, transparency, x and y adjustments, and image size can be adjusted by changing parameters
- Input and output folders can be adjusted by changing parameters
- Watermark image can be changed by updating the watermark path parameter
- Supports JPEG and PNG image formats
- Saves the adjusted image with the "GAIO_" prefix and series title and number
- Adjusts the image size based on value of max_width and max_height (which ever is less), and maintains image aspect ratio.


Here are the steps and features of the code:

1. Imports necessary modules: PIL, Image, ImageDraw, ImageFont, and os.
2. Sets various parameters for the watermark, including its path, size, transparency, and position.
3. Defines a function to add a watermark to an image. This function takes the image path, watermark path, size, transparency, position adjustments, series title, and file number as inputs.
4. The function opens both the image and watermark, resizes them as necessary, and adds transparency to the watermark.
5. The watermark is then blended with the image and saved to the output folder with a filename that includes the series title and file number.
6. Defines a function to resize an image proportionally based on either the maximum width or maximum height.
7. Lists all the input files in the input folder and sorts them alphabetically.
8. Loops through each input file, resizes it based on the maximum width and maximum height, and adds a watermark to it using the previously defined function.
9. Saves the watermarked images to the output folder.

Overall, the code reads image files from an input folder, resizes them, adds a watermark to them, and saves them to an output folder.


### How it started:

I asked ChatGPT to make it.  Most of the script was complete and running within a few minutes. A few hours more went into adjusting, debuggin, and optimizing it ...

![ChatGPT prompt and response](ChatGPT1.jpg)
