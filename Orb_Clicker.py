from pyautogui import *
import pyautogui
import keyboard
import win32api
import win32con
import math
import pygetwindow as gw

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

ROI = (255, 40, 951, 1004)
previousClick = None

Toggled = False  # Start with the script paused

while True:  # Run indefinitely
    if keyboard.is_pressed('pause'):
        Toggled = not Toggled  # Flip the toggled state
        time.sleep(0.1)  # Short delay to avoid bouncing the toggle
        
    if Toggled:
        # Check if the active window is "Final Fight"
        activeWindow = gw.getActiveWindow()
        if activeWindow is not None and activeWindow.title == 'Final Fight':
            location1 = pyautogui.locateOnScreen('NFFOrb1.png', confidence=0.6, grayscale=True, region=ROI)
            
            if location1 is not None:
                centerX = location1[0] + location1[2] // 2
                centerY = location1[1] + location1[3] // 2
                
                # Compare with the previous click location
                if (previousClick is None) or (distance(previousClick, (centerX, centerY)) > 25):
                    click(centerX, centerY)
                    previousClick = (centerX, centerY)
