import pygame
import sys
import evdev
from evdev import InputDevice, ecodes, list_devices
import select
from pprint import pprint as pp
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jeopardy Buzzer System')

# Define contestant names
contestants = ['Mouse 1', 'Mouse 2']

# To store the order of buzzes
buzz_order = []

# Find mouse devices
devices = [InputDevice(path) for path in list_devices()]
devices_with_names = [(device, device.name.lower()) for device in devices]
pp(devices_with_names)
mice_names = ['logitech mx vertical', 'logitech usb optical mouse']
mice = [device for device in devices if device.name.lower() in mice_names]

if len(mice) < 2:
    print("Please connect at least two mice.")
    sys.exit()

mouse1, mouse2 = mice[0], mice[1]

# Function to display the first buzzer
def display_first_buzzer(name):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render(name, True, (255, 255, 255))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()

# Start the game loop
running = True
while running:
    # Use select to handle multiple devices
    r, w, x = select.select([mouse1, mouse2], [], [], 0.01)

    for device in r:
        for event in device.read():
            if event.type == ecodes.EV_KEY and event.value == 1:  # 1 is key down
                if device == mouse1 and 'Mouse 1' not in buzz_order:
                    buzz_order.append('Mouse 1')
                    if len(buzz_order) == 1:
                        print(f"The first person to buzz in is: Mouse 1")
                        display_first_buzzer('Mouse 1')
                elif device == mouse2 and 'Mouse 2' not in buzz_order:
                    buzz_order.append('Mouse 2')
                    if len(buzz_order) == 1:
                        print(f"The first person to buzz in is: Mouse 2")
                        display_first_buzzer('Mouse 2')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(10)

pygame.quit()
sys.exit()
