"""
Day 6: Image Filtering & Blurring

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn image smoothing, noise reduction, and sharpening

Topics Covered:
1. Gaussian Blur
2. Median Blur
3. Sharpening Filters
4. Smoothing Noisy Images
5. Enhancing Image Clarity
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
# 1. Gaussian Blur
# ---------------------------------------------------
"""
Gaussian Blur smooths the image using a Gaussian kernel.
It reduces noise and detail.

Syntax:
cv2.GaussianBlur(image, (kernel_width, kernel_height), sigma)
"""

gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 2. Median Blur
# ---------------------------------------------------
"""
Median Blur replaces each pixel with the median value
of surrounding pixels.

Very effective for salt-and-pepper noise.
"""

median_blur = cv2.medianBlur(image, 7)

cv2.imshow("Median Blur", median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 3. Sharpening Filter
# ---------------------------------------------------
"""
Sharpening enhances edges and details.
We use a convolution kernel.
"""

sharpen_kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
])

sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 4. Smoothing Noisy Images
# ---------------------------------------------------
"""
Add artificial noise to demonstrate smoothing
"""

noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)

cv2.imshow("Noisy Image", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

smoothed_image = cv2.GaussianBlur(noisy_image, (9, 9), 0)

cv2.imshow("Smoothed Noisy Image", smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------
# 5. Enhancing Image Clarity
# ---------------------------------------------------
"""
Combining sharpening and smoothing
"""

blurred = cv2.GaussianBlur(image, (5, 5), 0)
enhanced_image = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

cv2.imshow("Enhanced Image", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Day 6 Goal Achieved ✔️

You learned:
- Gaussian blur for smoothing
- Median blur for noise removal
- Sharpening using kernels
- Noise reduction techniques
- Image clarity enhancement

Next Day:
Edge Detection & Contours (VERY IMPORTANT)
"""

