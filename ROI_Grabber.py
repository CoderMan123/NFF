import pyautogui
import time

print("Move your mouse over the top-left corner of your ROI and press Enter.")
input()  # Wait for Enter to be pressed
top_left = pyautogui.position()  # Get the position of the mouse

print("Move your mouse over the bottom-right corner of your ROI and press Enter.")
input()  # Wait for Enter to be pressed
bottom_right = pyautogui.position()  # Get the position of the mouse

# Calculate the width and height of the ROI
width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]

# Print out the ROI
print(f"Your ROI is: ({top_left[0]}, {top_left[1]}, {width}, {height})")
