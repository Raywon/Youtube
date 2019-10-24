import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.01
button = Button.left
start = KeyCode(char='1')
stop = KeyCode(char='2')
exitkey = KeyCode(char='3')
mouse = Controller()

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicker(self):
        self.running = True

    def stop_clicker(self):
        self.running = False

    def exit(self):
        self.stop_clicker()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start:
        click_thread.start_clicker()
        print("AutoMouse Start!")
    elif key == stop:
        click_thread.stop_clicker()
        print("AutoMouse Stop!")
    elif key == exitkey:
        click_thread.exit()
        print("Program Out!")
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()











        
