"""
Day 1: Introduction to OpenCV (Phase 0 – Getting Ready)

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Understanding OpenCV basics before coding

Topics Covered:
1. What is OpenCV?
2. Importance of Computer Vision
3. Where OpenCV is Used
4. Key Features of OpenCV
5. Prerequisites & Tools Setup
"""

# ---------------------------------------------------
# 1. What is OpenCV?
# ---------------------------------------------------
"""
OpenCV stands for Open Source Computer Vision Library.

It is an open-source library mainly used for:
- Image processing
- Video processing
- Computer vision
- Machine learning applications

OpenCV was originally developed by Intel and is now
maintained by the OpenCV community.
"""

# ---------------------------------------------------
# 2. Importance of Computer Vision
# ---------------------------------------------------
"""
Computer Vision enables machines to:
- See images
- Understand videos
- Detect objects
- Recognize faces
- Track movements

Without computer vision:
- Self-driving cars would not work
- Face unlock would not exist
- Medical image analysis would be impossible
"""

# ---------------------------------------------------
# 3. Where OpenCV is Used
# ---------------------------------------------------
"""
OpenCV is widely used in real-world applications such as:

1. Face Detection & Recognition
   - Phone face unlock
   - Attendance systems

2. Autonomous Vehicles
   - Lane detection
   - Obstacle detection

3. Medical Imaging
   - X-ray analysis
   - MRI image processing

4. Surveillance Systems
   - Motion detection
   - Person tracking

5. Augmented Reality (AR)
   - Filters (Snapchat / Instagram)
   - Virtual try-ons
"""

# ---------------------------------------------------
# 4. Key Features of OpenCV
# ---------------------------------------------------
"""
Major features of OpenCV include:

- Image & video reading/writing
- Image transformations (resize, rotate, crop)
- Object detection
- Face detection
- Feature detection
- Edge detection
- Contour detection
- Real-time video processing
- Works with Python, C++, Java

OpenCV is fast, efficient, and highly optimized.
"""

# ---------------------------------------------------
# 5. Prerequisites & Tools Setup
# ---------------------------------------------------
"""
Before starting OpenCV, you should have:

Prerequisites:
- Basic Python knowledge
- Understanding of arrays (NumPy)
- Basic idea of images as matrices

Tools Required:
- Python 3.x
- pip (Python package manager)
- OpenCV library
- NumPy library
- Code Editor (VS Code recommended)

Installation Command:
pip install opencv-python
pip install numpy
"""

# ---------------------------------------------------
# 6. Checking OpenCV Installation
# ---------------------------------------------------
import cv2

print("OpenCV Version:", cv2.__version__)

"""
If the version prints successfully,
OpenCV is installed correctly.

Day 1 Goal Achieved ✔️
Next Day: Reading & displaying images using OpenCV
"""
