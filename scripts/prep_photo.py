import sys
import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def prep_photo(input_path, output_path="source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Error: '{input_path}' not found.")
        sys.exit(1)

    print(f"1. Loading {input_path}...")
    img = cv2.imread(input_path)

    # --- Crop to person: lower 65% of the photo ---
    h, w = img.shape[:2]
    crop_y = int(h * 0.38)
    # Also crop sides slightly
    crop_x = int(w * 0.05)
    cropped = img[crop_y:, crop_x: w - crop_x]

    print("2. Converting to grayscale and boosting contrast...")
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    # CLAHE for local contrast boost (great for night photos)
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Gamma correction to brighten the subject
    gamma = 1.6
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)]).astype("uint8")
    gamma_corrected = cv2.LUT(enhanced, table)

    # Sharpen
    kernel = np.array([[0, -0.5, 0], [-0.5, 3, -0.5], [0, -0.5, 0]])
    sharpened = cv2.filter2D(gamma_corrected, -1, kernel)

    # Scale to a square for better ASCII output
    final = cv2.resize(sharpened, (512, 512), interpolation=cv2.INTER_LANCZOS4)

    # Composite onto white background (so dark BG → spaces in ASCII)
    out_pil = Image.fromarray(final).convert("L")
    out_pil.save(output_path)
    print(f"3. Saved prepped image to '{output_path}'!")

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(inp)
