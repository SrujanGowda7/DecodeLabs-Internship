import cv2
import pytesseract
from PIL import Image

# For macOS (Homebrew installation)
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

print("=" * 50)
print("      Image Text Recognition (OCR)")
print("=" * 50)

image_path = input("Enter image file name (Example: sample_text.png): ")

try:
    # Read image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
    else:
        # Convert image to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Extract text
        extracted_text = pytesseract.image_to_string(rgb_image)

        print("\nExtracted Text:")
        print("-" * 50)
        print(extracted_text)
        print("-" * 50)

except Exception as e:
    print("An error occurred:", e)