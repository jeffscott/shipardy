import select
import time
import pygame as pg
from gamescreen import GameBoard
from evdev import ecodes
from pprint import pprint as pp

from device import DeviceManager

BUZZER_TIMEOUT_SEC = 10


if __name__ == "__main__":

    contestant_map = {
        'Logitech MX Vertical': 'Snaptician',
        'Logitech USB Optical Mouse': 'Cool Aunt Leez',
        'Logitech Wireless Receiver Mouse': 'Djeff Djon Dert Muv'
    }

    dev_manager = DeviceManager()
    dev_manager.print_devices()
    dev_manager.print_contestants()
    for device, contestant in contestant_map.items():
        dev_manager.assign_contestant(contestant, device) 
    dev_manager.print_contestants()
    print(dev_manager.get_contestant_devices())

    pg.init()

    board = GameBoard()

    running = True
    buzzin_active = False 
    buzz_order = []
    current_contestant = None
    time_start = 0
    time_end = 0
    while running:

        r, w, x = select.select(dev_manager.get_contestant_devices(), [], [], 0.01)

        """ 
        EV_KEY is button press value 1 is down

        When round is active, if any button is pressed, append the device
        if it's not already in the list

        After the buzz in is over, stop checking for new device events
        """
        for event in pg.event.get():

            if event.type == pg.KEYDOWN and event.key == pg.K_q: 
                running = False
            # START BUZZIN
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print('BUZZER OPEN!')
                buzzin_active = True
                buzz_order = []
                time_start = time.time()
                board.display_buzzer_window()
                board.display_buzzer_active()


            if event.type == pygame.QUIT:
                running = False

        # TIMEOUT AFTER SOME PERIOD
        if buzzin_active:
            if time.time() - time_start > BUZZER_TIMEOUT_SEC:
                buzzin_active = False
                board.display_buzzer_window()
                print('BUZZIN CLOSED!', flush=True)
        else:
            for c, device_name in enumerate(buzz_order):
                board.display_player_name(contestant_map[device_name], c)



        # GET THE CLICK ORDER OF EACH SUPPORTED DEVICE AFTER BUZZIN STARTS
        for device in r:
            for event in device.read():
                if event.type == ecodes.EV_KEY and event.value == 1:  # 1 is key down
                    print(event)
                    if buzzin_active is True and device.name not in buzz_order:
                        buzz_order.append(device.name)
                        print(buzz_order)
                    
                        if len(buzz_order) == len(contestant_map.keys()):
                            print('BUZZIN CLOSED!', flush=True)
                            board.display_buzzer_window()
                            buzzin_active = False

