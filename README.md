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

5. Run the script: Open your terminal or command prompt, navigate to the directory where the script is located, and run the script by running the following command: `python3 autosig.py`

6. Check the output: The script will save the processed images with the watermark in a folder named `_output`. Check this folder to see the results.


### Features:

- Adds a PNG watermark to images in a specified folder
- Watermark size, transparency, x and y adjustments can be adjusted by changing parameters
- Input and output folders can be adjusted by changing parameters
- Watermark image can be changed by updating the watermark path parameter
- Supports JPEG and PNG image formats
- Saves the adjusted image with the "GAIO_" prefix and series title and number



The steps of the code:

1. Import necessary modules - the PIL (Python Imaging Library) module and the os module.
2. Define a function to add a watermark to an image.
   - The function takes in the path of the image and the path of the watermark, along with several other parameters.
   - The function opens the image and watermark, resizes the watermark to the desired size, adds transparency to the watermark, and blends the watermark with the image.
   - If the image is not in RGB mode, the function converts it to RGB mode.
   - The function saves the adjusted image with the "GAIO_" prefix and series title and number.
3. Set parameters for the watermark and its positioning, as well as for the input and output folders.
4. Get a sorted list of input files in the input folder.
5. Loop through all the images in the input folder.
   - For each image, call the add_watermark function with the image path and the watermark path and other parameters to add the watermark.
   - Increment the file number counter.
6. Print out the paths of the processed files and output files.

The features of the code:

- Opens images and watermarks using the PIL module.
- Resizes watermarks using the resize() method.
- Adds transparency to watermarks using the putalpha() method.
- Blends watermarks with images using the alpha_composite() method.
- Converts images to RGB mode if necessary using the convert() method.
- Saves adjusted images using the save() method.
- Handles exceptions using a try-except block.
- Prints out information about processed files and output files.


### How it started:

I asked ChatGPT to make it.  Most of the script was complete and running within a few minutes. A few hours more went into adjusting, debuggin, and optimizing it ...

![ChatGPT prompt and response](ChatGPT1.jpg)
