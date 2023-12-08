from PIL import Image
import os

# User input
imagepath = input("Path to image: ")

# Open & Convert
im = Image.open(imagepath)
im.convert('RGBA').convert('P', palette=Image.ADAPTIVE, colors=255)

# Get filename from path & save
head, tail = os.path.split(imagepath)
im.save(tail.replace(".webp", ".png"), "png")
print("Done!")