#Default actions:   left click, drag, double click
#First param:       action
#Second param:      coordinate
from proj_overlay import *
import keyboard
import mouse
import time
#Mouse strategy:    Get current screen dimension
#                   Determine the locations of some buttons (e.g. windows, close, minimize)
#                   Scale those locations to current screen

#Most defining function: show the grid with num_box boxes
def show_grid(num_box):
    return 0

def drag(start_pos, end_pos):
    return 0

def left_click(position): #Either corners or a box on the grid
    return 0

def scroll_down():
    return 0

def scroll_up():
    return 0
    
def press_window():
    keyboard.press_and_release("windows")
    return 0

def maximize():
    #Double click the top program bar
    #Location: (middle of the bar, top - 5)
    #Program bar + other specs can be acquired by tkinter
    return 0
    
def run(query):
    keyboard.press_and_release("windows+R")
    keyboard.type(query)
    keyboard.press_and_release("enter")
    return 0

def search(query): #Opens the default browser and search for query
    return 0

def pause(): #Space
    return 0

def quit_current(): #Quit currently active window. Do we have to alt+tab to it?
    keyboard.press_and_release("alt+F4")
    return 0

def minimize():
    return 0

def show_desktop(): #Windows+M
    keyboard.press_and_release("Windows+m")
    return 0

#Navigation on Youtube
def yt_next(): #Shift N
    keyboard.press_and_release("shift+n")
    return 0

def yt_previous():#Shift P
    keyboard.press_and_release("shift+p")
    return 0

def yt_fullscreen():#F
    keyboard.press_and_release("f")
    return 0

#Below are actions that would trigger a voiced response
#Queue 'weather' on default browser and read aloud the result
def weather():
    return 0

def ask_wiki(query):
    return 0