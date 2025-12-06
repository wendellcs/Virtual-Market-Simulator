from tkinter import *

frames = {
    'login': None,
    'register': None,
    'home': None,
}

def set_frame(frame_name, frame):
    frames[frame_name] = frame

def show_screen(frame_name):
    frames[frame_name].tkraise()