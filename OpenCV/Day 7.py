"""
Day 7: Edge Detection & Thresholding

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn edge detection, thresholding, and masking techniques

Topics Covered:
1. Canny Edge Detection
2. Binary Thresholding
3. Adaptive Thresholding
4. Bitwise Operations (AND, OR, NOT)
5. Extracting outlines from images
"""

import cv2
import numpy as np

# ---------------------------------------------------
# Load Image
# ---------------------------------------------------
image = cv2.imread("sample.jpg")  # Replace with your image path

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 1. Canny Edge Detection
# ---------------------------------------------------
"""
Canny detects strong edges in an image.
It works best on grayscale images.
"""

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 2. Binary Thresholding
# ---------------------------------------------------
"""
Thresholding converts grayscale image to binary (black & white)
"""

_, binary_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Thresholding", binary_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 3. Adaptive Thresholding
# ---------------------------------------------------
"""
Adaptive threshold works well in varying lighting conditions
"""

adaptive_thresh = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Adaptive Thresholding", adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Bitwise Operations
# ---------------------------------------------------
"""
Used for masking and combining images
"""

# Create a mask using threshold
mask = adaptive_thresh

# Bitwise AND
and_result = cv2.bitwise_and(image, image, mask=mask)

# Bitwise OR
or_result = cv2.bitwise_or(image, image, mask=mask)

# Bitwise NOT
not_result = cv2.bitwise_not(mask)

cv2.imshow("Bitwise AND", and_result)
cv2.imshow("Bitwise OR", or_result)
cv2.imshow("Bitwise NOT", not_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 5. Extracting Outlines from Image
# ---------------------------------------------------
"""
Outlines can be extracted using edges or thresholded image
"""

outlines = cv2.Canny(gray, 50, 150)

cv2.imshow("Extracted Outlines", outlines)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Day 7 Goal Achieved ✔️

You learned:
- Canny edge detection
- Binary & adaptive thresholding
- Bitwise image operations
- Outline extraction techniques

Next Day:
Contours detection & shape analysis
"""

