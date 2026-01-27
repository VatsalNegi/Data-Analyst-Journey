"""
Day 5: Working with Video & Webcam

Author: Vatsal Negi
Domain: Computer Vision / AI
Purpose: Learn video capture, real-time processing, and video saving

Topics Covered:
1. Capturing video from webcam
2. Frame-by-frame processing
3. Applying real-time filters
4. Saving video using VideoWriter
"""

import cv2

# ---------------------------------------------------
# 1. Capturing Video from Webcam
# ---------------------------------------------------
"""
cv2.VideoCapture(0)
0 -> default webcam
1 -> external webcam (if available)
"""

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Webcam opened successfully")

# ---------------------------------------------------
# 2. Video Writer (Saving Video)
# ---------------------------------------------------
"""
VideoWriter parameters:
- filename
- codec (fourcc)
- frames per second
- frame size (width, height)
"""

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    "output_video.avi",
    fourcc,
    20.0,
    (640, 480)
)

# ---------------------------------------------------
# 3. Frame-by-Frame Processing
# ---------------------------------------------------
"""
Video is a sequence of images (frames)
We read and process each frame one by one
"""

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # ---------------------------------------------------
    # 4. Real-Time Filters
    # ---------------------------------------------------

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Edge detection using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Convert edges to BGR for saving video
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Write frame to video file
    out.write(edges_bgr)

    # Display outputs
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Grayscale Frame", gray)
    cv2.imshow("Edge Detection", edges)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------------------------------------------
# 5. Release Resources
# ---------------------------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()

"""
Day 5 Goal Achieved ✔️

You learned:
- Capturing video from webcam
- Reading video frame-by-frame
- Applying real-time filters
- Saving processed video to file

Next Day:
Color spaces (RGB vs HSV), color detection & masking
"""

