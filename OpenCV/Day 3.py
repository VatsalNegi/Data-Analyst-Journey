"""
Day 3: Image Transformations & Manipulation

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn how to manipulate images using OpenCV

Topics Covered:
1. Resizing & scaling images
2. Cropping images using slicing
3. Rotating images
4. Flipping images
5. Drawing shapes (line, rectangle, circle)
6. Adding text on images
"""

import cv2

# ---------------------------------------------------
# Load Image
# ---------------------------------------------------
image = cv2.imread("sample.jpg")  # Replace with your image path

if image is None:
    print("Error: Image not found!")
    exit()

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 1. Resizing & Scaling Images
# ---------------------------------------------------
"""
cv2.resize() is used to resize an image.

Syntax:
resized = cv2.resize(image, (width, height))
"""

resized_image = cv2.resize(image, (300, 300))
cv2.imshow("Resized Image (300x300)", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Scaling using fx and fy
"""

scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow("Scaled Image (50%)", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 2. Cropping Image using Slicing
# ---------------------------------------------------
"""
Image is a NumPy array.
Slicing format:
image[y1:y2, x1:x2]
"""

cropped_image = image[50:300, 100:400]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 3. Rotating an Image
# ---------------------------------------------------
"""
Rotation requires:
- Center of image
- Angle
- Scale
"""

height, width = image.shape[:2]
center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image (45 degrees)", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Flipping an Image
# ---------------------------------------------------
"""
flipCode:
0  -> Vertical flip
1  -> Horizontal flip
-1 -> Both axes
"""

horizontal_flip = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", horizontal_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

vertical_flip = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", vertical_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 5. Drawing Shapes on Image
# ---------------------------------------------------
"""
All drawing is done on a copy of image
Color format: (B, G, R)
"""

draw_img = image.copy()

# Draw Line
cv2.line(draw_img, (50, 50), (300, 50), (0, 255, 0), 2)

# Draw Rectangle
cv2.rectangle(draw_img, (50, 100), (300, 250), (255, 0, 0), 2)

# Draw Circle
cv2.circle(draw_img, (200, 350), 40, (0, 0, 255), -1)

cv2.imshow("Drawing Shapes", draw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 6. Adding Text on Image
# ---------------------------------------------------
"""
cv2.putText() adds text to image
"""

text_img = image.copy()

cv2.putText(
    text_img,
    "OpenCV Day 3",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Text on Image", text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Day 3 Goal Achieved ✔️

You learned:
- Resizing & scaling
- Cropping with slicing
- Rotating & flipping
- Drawing shapes
- Adding text to images

Next Day:
Image filtering, blurring, edge detection (Canny)
"""

