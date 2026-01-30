"""
Day 8: Contours & Shape Detection

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn contour detection, shape identification, and basic object recognition

Topics Covered:
1. Finding contours
2. Drawing contours on images
3. Shape detection using approxPolyDP
4. Basic object recognition using shapes
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
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# Preprocessing for Contours
# ---------------------------------------------------
"""
Contours work best on binary images
"""

blur = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 1. Finding Contours
# ---------------------------------------------------
"""
cv2.findContours() detects boundaries of objects

RETR_EXTERNAL -> retrieves only outer contours
CHAIN_APPROX_SIMPLE -> removes redundant points
"""

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours found:", len(contours))

# ---------------------------------------------------
# 2. Drawing Contours on Image
# ---------------------------------------------------
contour_img = image.copy()

cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

cv2.imshow("All Contours", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 3. Shape Detection using approxPolyDP
# ---------------------------------------------------
"""
approxPolyDP approximates contour shape
Based on number of vertices, we detect shape
"""

shape_img = image.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)

    # Ignore very small contours (noise)
    if area < 500:
        continue

    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)

    x, y, w, h = cv2.boundingRect(approx)

    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        aspect_ratio = w / float(h)
        if 0.95 < aspect_ratio < 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"
    elif len(approx) == 5:
        shape = "Pentagon"
    else:
        shape = "Circle"

    # Draw contour and label
    cv2.drawContours(shape_img, [approx], -1, (255, 0, 0), 2)
    cv2.putText(
        shape_img,
        shape,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

cv2.imshow("Shape Detection", shape_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Basic Object Recognition (Using Shape + Area)
# ---------------------------------------------------
"""
Basic object recognition is done using:
- Shape
- Area
- Position
"""

object_img = image.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area > 2000:
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(object_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            object_img,
            "Object",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

cv2.imshow("Basic Object Recognition", object_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Day 8 Goal Achieved ✔️

You learned:
- Finding contours
- Drawing contours
- Shape detection using approxPolyDP
- Basic object recognition

Next Day:
Color spaces (HSV) & color-based object detection
"""

