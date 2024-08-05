## Ghost

<img width="504" alt="Screenshot 2024-08-05 at 6 40 03 AM" src="https://github.com/user-attachments/assets/42a5e235-aa62-4164-830f-64ecd7773f67">

## Description
Ghost is a Python program designed to manipulate pixels to create unique images. 
It accomplishes this by taking a series of similar images and combining them to create a new image where the people from the original images are "ghosted out." <br>

Ghost works by comparing each pixel across all the images in the provided directory. It calculates the "distance" between a pixel's RGB value and the average RGB value of all pixels at that location across all images. The pixel closest to the average in each location is chosen for the final image. This process creates a new image where the people (who would have caused significant variations in pixel values across the image set) are "ghosted out."

This repository includes two additional Python programs that manipulate images:

* **warhol.py:** This program takes an image and creates a pop-art style image similar to Andy Warhol's work.
* **forestfire.py:** This program analyzes an image and attempts to highlight potential fire areas by identifying pixels with a strong red value.

## Technologies Used
* Python
* SimpleImage

## Installation
Before running the Ghost program, you'll need to install the SimpleImage library using pip:

```Bash
pip install simpleimage
```

## Usage
Once SimpleImage is installed, you can use Ghost from the command line. Here's the syntax:

```Bash
python3 ghost.py <directory_name>
```
Replace <directory_name> with the actual name of the directory containing your set of similar images. For example:

```Bash
python3 ghost.py family_portraits
```

This will process the images in the "family_portraits" directory and create a new image where the people are removed, leaving a ghostly trace.
