import cv2 as cv


import numpy as np

def detect_roulette_numbers(frame):
    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply a median blur to reduce noise
    blurred = cv.medianBlur(gray, 5)

    # Apply a Canny edge detector to detect edges
    edges = cv.Canny(blurred, 50, 150)

    # Find contours in the edges
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for contour in contours:
        # Approximate the contour
        approx = cv.approxPolyDP(contour, 0.02 * cv.arcLength(contour, True), True)

        # If the contour has 4 sides, it is a rectangle
        if len(approx) == 4:
            # Get the coordinates of the rectangle
            x, y, w, h = cv.boundingRect(approx)

            # If the rectangle is large enough, it is a roulette number
            if w > 100 and h > 100:
                # Get the center of the rectangle
                center = (x + w // 2, y + h // 2)

                # Return the center of the rectangle
                return center

    # If no roulette numbers are found, return None
    return None

# Reading Videos
capture = cv.VideoCapture("Testvidoes/Roulette_Wheel_Spinning.mp4")

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()

    # If the frame was read successfully
    if isTrue:
        # Detect roulette numbers in the frame
        center = detect_roulette_numbers(frame)

        # If a roulette number was detected
        if center is not None:
            # Draw a circle at the center of the detected roulette number
            cv.circle(frame, center, 10, (0, 255, 0), -1)

        # Display the frame
        cv.imshow("Video", frame)

    # If the 'd' key is pressed, break the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()