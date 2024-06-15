import pygame
import select
import pygame as pg
from queue import Queue
from evdev import ecodes
from pprint import pprint as pp

from device import DeviceManager



def pygame_setup():

    pg.init()

    # Set up the display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Jeopardy Buzzer System')

if __name__ == "__main__":


    dev_manager = DeviceManager()
    dev_manager.print_devices()
    dev_manager.print_contestants()

    dev_manager.assign_contestant('Snaptician', 'Logitech MX Vertical')
    dev_manager.assign_contestant('Cool Aunt Leez', 'Logitech USB Optical Mouse')
    dev_manager.print_contestants()

    pygame_setup()

    contestant_queue = Queue()
    running = True
    round_active = True 
    while running:

        r, w, x = select.select(dev_manager.get_contestant_devices(), [], [], 0.01)
        if round_active is True:
            for device in r:
                for event in device.read():
                    # EV_KEY is button press value 1 is down
                    if event.type == ecodes.EV_KEY and event.value == 1:  # 1 is key down
                        print(device.name)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False