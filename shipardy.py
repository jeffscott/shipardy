import select
import time
import pygame as pg
import argparse
from gamescreen import GameBoard
from evdev import ecodes
from pprint import pprint as pp

from device import DeviceManager

BUZZER_TIMEOUT_SEC = 10


def main(args):

    dev_manager = DeviceManager()
    if args.print_input_devices:
        dev_manager.list_available_devices()
        exit()

    contestant_map = {
        'usb-0000:0e:00.0-2.4/input0': 'Player1',
        'usb-0000:0e:00.0-2.3/input0': 'Player2',
        'usb-0000:0e:00.0-2.2/input0': 'Player3',
        'usb-0000:0e:00.0-3/input2:1': 'Player4',

    }
    for device, contestant in contestant_map.items():
        print(device)
        dev_manager.assign_contestant(contestant, device) 
    dev_manager.print_contestants()

    pg.init()
    board = GameBoard()

    running = True
    buzzin_active = False 
    buzz_order = []
    time_start = 0
    while running:


        """ 
        EV_KEY is button press value, 1 is down

        When round is active, if any button is pressed, append the device
        if it's not already in the list

        After the buzz in is over, stop checking for new device events and
        display the order of contestant buzzin
        """
        # GET THE CLICK ORDER OF EACH SUPPORTED DEVICE AFTER BUZZIN STARTS
        r, w, x = select.select(dev_manager.get_contestant_devices(), [], [], 0.01)
        for device in r:
            for event in device.read():
                if event.type == ecodes.EV_KEY and event.value == 1:  # 1 is key down
                    print(event)
                    if buzzin_active is True and device.phys not in buzz_order:
                        buzz_order.append(device.phys)
                        print(buzz_order)
                    
                        if len(buzz_order) == len(contestant_map.keys()):
                            print('BUZZIN CLOSED!', flush=True)
                            board.display_buzzer_window()
                            buzzin_active = False

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


            if event.type == pg.QUIT:
                running = False

        # TIMEOUT AFTER SOME PERIOD
        if buzzin_active:
            if time.time() - time_start > BUZZER_TIMEOUT_SEC:
                buzzin_active = False
                board.display_buzzer_window()
                print('BUZZIN CLOSED!', flush=True)
        else:
            for c, device_phys in enumerate(buzz_order):
                board.display_player_name(contestant_map[device_phys], c)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Shipardy buzzer program")

    parser.add_argument("--print-input-devices", "-p", action='store_true', help="Print the available devices for use")
    args = parser.parse_args()

    main(args)
