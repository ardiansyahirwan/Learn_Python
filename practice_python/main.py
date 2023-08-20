from greeting_independence_day import say_about_independence_day
import pyautogui
import keyboard

msg = say_about_independence_day()
name = "Broo"

pyautogui.moveTo(1180,733)
pyautogui.click()
pyautogui.write(message=f"Hi.. {name} {msg}")
keyboard.press("enter")

# yuk dicobaaaaaa