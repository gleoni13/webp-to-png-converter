import os
from PIL import Image

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(current_dir)

count = 0

# Loop through all files in the directory
for file in os.listdir('.'):
    if file.lower().endswith('.webp'):
        # Open the WebP image
        img = Image.open(file)
        
        # Generate the new filename by replacing the extension
        png_name = os.path.splitext(file)[0] + '.png'
        
        # Save in PNG format
        img.save(png_name, 'PNG')
        count += 1
        print(f"Converted: {file} -> {png_name}")

print(f"\nDone! Successfully converted {count} images.")
