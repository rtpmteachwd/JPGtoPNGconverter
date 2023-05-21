import sys
import os
from PIL import Image

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Please provide the source folder path and the destination folder path as command-line arguments.")
    sys.exit(1)

# Grab the first and second command-line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Check if the destination folder exists, if not, create it
if not os.path.exists(arg2):
    os.makedirs(arg2)
    print("Directory created:", arg2)
else:
    print("Directory already exists:", arg2)

# Loop through the source folder
for filename in os.listdir(arg1):
    if filename.endswith(".jpg"):
        file_path = os.path.join(arg1, filename)

        # Open the image using PIL
        image = Image.open(file_path)

        # Convert the image to PNG
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_file_path = os.path.join(arg2, new_filename)
        image.save(new_file_path, "PNG")

        # Close the image
        image.close()

print("Image conversion completed.")