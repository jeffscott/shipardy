# Shipardy!

## Requirements
python 3.10.X

Install packages, it's recommended to use a venv

```
pip install -r requirements.txt
```

## Running
You need to run the script as root for the devices to be detected use `sudo`. You can explicitly run the python version in the virtual environment:

```
sudo ~/python-environments/shipardy/bin/python shipardy.py
```

## Multiple Mice Setup

Run the script to get the mouse names, this is the devices in `/dev/input`
```
[(InputDevice('/dev/input/event7'), 'logitech usb optical mouse'),
 (InputDevice('/dev/input/event17'),
  'input-remapper kinesis corporation kb800hm kinesis freestyle2 for mac '
  'forwarded'),
 (InputDevice('/dev/input/event16'), 'input-remapper keyboard'),
 (InputDevice('/dev/input/event15'), 'hda nvidia hdmi/dp,pcm=9'),
 (InputDevice('/dev/input/event14'), 'hda nvidia hdmi/dp,pcm=8'),
 (InputDevice('/dev/input/event13'), 'hda nvidia hdmi/dp,pcm=7'),
 (InputDevice('/dev/input/event12'), 'hda nvidia hdmi/dp,pcm=3'),
 (InputDevice('/dev/input/event10'), 'hd-audio generic hdmi/dp,pcm=9'),
 (InputDevice('/dev/input/event9'), 'hd-audio generic hdmi/dp,pcm=8'),
 (InputDevice('/dev/input/event8'), 'hd-audio generic hdmi/dp,pcm=7'),
 (InputDevice('/dev/input/event6'), 'hd-audio generic hdmi/dp,pcm=3'),
 (InputDevice('/dev/input/event5'), 'logitech mx vertical'),
 (InputDevice('/dev/input/event4'),
  'kinesis corporation kb800hm kinesis freestyle2 for mac'),
 (InputDevice('/dev/input/event3'),
  'kinesis corporation kb800hm kinesis freestyle2 for mac'),
 (InputDevice('/dev/input/event11'), 'msi mystic light '),
 (InputDevice('/dev/input/event2'), 'video bus'),
 (InputDevice('/dev/input/event1'), 'power button'),
 (InputDevice('/dev/input/event0'), 'power button')]
```
Replace the names in the variable `mice_names` with the names of the input devices above, in this case `logitech usb optical mouse` and `logitech mx vertical`.
