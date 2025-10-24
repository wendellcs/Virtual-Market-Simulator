import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep(seconds = 3):
    time.sleep(seconds)