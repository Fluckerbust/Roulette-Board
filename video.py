import cv2
import numpy as np

# Define a function to detect roulette numbers
def detect_roulette_numbers(frame):
  # Convert the frame to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Apply a median blur to remove noise
  blurred = cv2.medianBlur(gray, 5)

  # Apply a Canny edge detector to detect edges
  edges = cv2.Canny(blurred, 50, 150)

  # Find contours in the edges
  contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Loop through the contours
  for contour in contours[1]:
    # Approximate the contour
    approx = cv2.approxPolyDP(contour, 0.02, True)

    # If the contour has 4 sides, it is a rectangle
    if len(approx) == 4:
      # Get the coordinates of the rectangle
      (x, y, w, h) = cv2.boundingRect(approx)

      # If the rectangle is large enough, it is a roulette number
      if w > 100 and h > 100:
        # Get the center of the rectangle
        center = (x + w / 2, y + h / 2)

        # Return the center of the rectangle
        return center

  # If no roulette numbers are found, return None
  return None

# Start the webcam
cap = cv2.VideoCapture(0)

# Loop until the user presses the Esc key
