"""
Day 4: Basic Image Drawing Techniques

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn how to draw shapes, text, and overlays on images

Topics Covered:
1. Drawing lines
2. Drawing rectangles
3. Drawing circles
4. Adding custom text
5. Creating basic graphic overlays
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

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 1. Drawing Lines
# ---------------------------------------------------
"""
cv2.line(image, start_point, end_point, color, thickness)
Color format: (B, G, R)
"""

line_img = image.copy()

cv2.line(line_img, (50, 50), (400, 50), (0, 255, 0), 3)
cv2.line(line_img, (50, 100), (400, 200), (255, 0, 0), 2)

cv2.imshow("Drawing Lines", line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 2. Drawing Rectangles
# ---------------------------------------------------
"""
cv2.rectangle(image, top_left, bottom_right, color, thickness)
Use thickness = -1 for filled rectangle
"""

rect_img = image.copy()

cv2.rectangle(rect_img, (50, 50), (300, 200), (0, 0, 255), 2)
cv2.rectangle(rect_img, (350, 50), (550, 200), (255, 0, 0), -1)

cv2.imshow("Drawing Rectangles", rect_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 3. Drawing Circles
# ---------------------------------------------------
"""
cv2.circle(image, center, radius, color, thickness)
"""

circle_img = image.copy()

cv2.circle(circle_img, (200, 300), 50, (0, 255, 255), 3)
cv2.circle(circle_img, (400, 300), 40, (255, 0, 255), -1)

cv2.imshow("Drawing Circles", circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Adding Custom Text on Image
# ---------------------------------------------------
"""
cv2.putText(
    image,
    text,
    position,
    font,
    font_scale,
    color,
    thickness
)
"""

text_img = image.copy()

cv2.putText(
    text_img,
    "OpenCV - Day 4",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.putText(
    text_img,
    "Drawing & Overlays",
    (50, 100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (0, 255, 0),
    2
)

cv2.imshow("Adding Text", text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 5. Creating Basic Graphic Overlays
# ---------------------------------------------------
"""
Overlay = semi-transparent graphics on image
"""

overlay = image.copy()
output = image.copy()

# Draw filled rectangle on overlay
cv2.rectangle(overlay, (0, 0), (image.shape[1], 80), (0, 0, 0), -1)

# Alpha blending
alpha = 0.5
cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

# Add text on overlay
cv2.putText(
    output,
    "Status: Processing Image",
    (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 255),
    2
)

cv2.imshow("Graphic Overlay", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Day 4 Goal Achieved ✔️

You learned:
- Drawing lines, rectangles, circles
- Using thickness & filled shapes
- Adding custom text
- Creating semi-transparent overlays

Next Day:
Color spaces (RGB, HSV), color detection & masking
"""

