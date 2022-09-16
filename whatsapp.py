import pyautogui as pt
import time
import pytesseract


limit = input("Enter limit : ")
message =input("Enter message : ")
i=0
time.sleep(5)
while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i=i+1


