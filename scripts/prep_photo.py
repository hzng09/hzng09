import sys
import os
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_image_path, output_image_path="source-prepped.png"):
    if not os.path.exists(input_image_path):
        print(f"Error: Input file '{input_image_path}' not found.")
        sys.exit(1)
        
    print(f"1. Removing background from {input_image_path}...")
    input_img = Image.open(input_image_path)
    output_rgba = remove(input_img)
    
    print("2. Compositing onto white background & boosting contrast...")
    white_bg = Image.new("RGBA", output_rgba.size, (255, 255, 255, 255))
    composited = Image.alpha_composite(white_bg, output_rgba).convert("L")
    
    img_np = np.array(composited)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    enhanced_np = clahe.apply(img_np)
    
    enhanced_img = Image.fromarray(enhanced_np)
    enhanced_img.save(output_image_path)
    print(f"3. Saved prepped grayscale image to '{output_image_path}'!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py <path-to-photo.jpg>")
    else:
        prep_photo(sys.argv[1])
