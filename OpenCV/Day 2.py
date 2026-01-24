"""
Day 2: Getting Started with OpenCV

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn basic image operations using OpenCV

Topics Covered:
1. Installing OpenCV (cv2)
2. Reading an image
3. Displaying an image
4. Saving an image
5. Image dimensions & channels
6. Grayscale conversion
"""

# ---------------------------------------------------
# 1. Installing OpenCV
# ---------------------------------------------------
"""
If OpenCV is not installed, run this command in terminal:

pip install opencv-python

OpenCV is imported as cv2 in Python.
"""

import cv2

# ---------------------------------------------------
# 2. Reading an Image
# ---------------------------------------------------
"""
cv2.imread() is used to read an image.

Syntax:
image = cv2.imread("image_path")

- It returns the image as a NumPy array
- If the path is wrong, it returns None
"""

image = cv2.imread("sample.jpg")  # Replace with your image path

# Check if image is loaded properly
if image is None:
    print("Error: Image not found!")
    exit()
else:
    print("Image loaded successfully")

# ---------------------------------------------------
# 3. Displaying an Image
# ---------------------------------------------------
"""
cv2.imshow() displays the image in a window.

Syntax:
cv2.imshow("Window Name", image)

cv2.waitKey(0) waits until a key is pressed
cv2.destroyAllWindows() closes all windows
"""

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Saving an Image
# ---------------------------------------------------
"""
cv2.imwrite() saves an image to disk.

Syntax:
cv2.imwrite("filename.jpg", image)
"""

cv2.imwrite("saved_image.jpg", image)
print("Image saved successfully")

# ---------------------------------------------------
# 5. Image Dimensions & Channels
# ---------------------------------------------------
"""
image.shape returns:
(height, width, channels)

- Height → number of rows
- Width  → number of columns
- Channels → color information (BGR)
"""

height, width, channels = image.shape

print("Image Height:", height)
print("Image Width:", width)
print("Number of Channels:", channels)

"""
Note:
- Color image → 3 channels (BGR)
- Grayscale image → 1 channel
"""

# ---------------------------------------------------
# 6. Grayscale Conversion
# ---------------------------------------------------
"""
Grayscale image has only intensity information.

cv2.cvtColor() is used to convert color spaces.

Syntax:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
"""

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save grayscale image
cv2.imwrite("grayscale_image.jpg", gray_image)
print("Grayscale image saved successfully")

"""
Day 2 Goal Achieved ✔️

You learned:
- How to read images
- How to display images
- How to save images
- Image dimensions & channels
- Grayscale conversion

Next Day:
Image resizing, cropping, flipping & basic transformations
"""

