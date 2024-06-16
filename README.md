# Shipardy!

## Requirements
python 3.10.X

Install packages, it's recommended to use a venv

```
sudo apt-get install python3-dev
```

```
pip install -r requirements.txt
```

## Running
You need to run the script as root for the devices to be detected use `sudo`. You can explicitly run the python version in the virtual environment. This path will change depending on where your virtual environment is.

```
sudo ~/python-environments/shipardy/bin/python shipardy.py
```

## Multiple Mice Setup

Run the script to get the mouse names, this is the devices in `/dev/input` and you can print out what the program sees via:
```
sudo ~/python-environments/shipardy/bin/python shipardy.py -p
```

```
[('Logitech USB Optical Mouse', 'usb-0000:0e:00.0-2.4/input0'),
 ('Logitech USB Laser Mouse', 'usb-0000:0e:00.0-2.3/input0'),
 ('Logitech USB-PS/2 Optical Mouse', 'usb-0000:0e:00.0-2.2/input0'),
 ('input-remapper KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac '
  'forwarded',
  'py-evdev-uinput'),
 ('input-remapper keyboard', 'input-remapper'),
 ('HDA NVidia HDMI/DP,pcm=9', 'ALSA'),
 ('HDA NVidia HDMI/DP,pcm=8', 'ALSA'),
 ('HDA NVidia HDMI/DP,pcm=7', 'ALSA'),
 ('HDA NVidia HDMI/DP,pcm=3', 'ALSA'),
 ('HD-Audio Generic HDMI/DP,pcm=9', 'ALSA'),
 ('HD-Audio Generic HDMI/DP,pcm=8', 'ALSA'),
 ('HD-Audio Generic HDMI/DP,pcm=7', 'ALSA'),
 ('HD-Audio Generic HDMI/DP,pcm=3', 'ALSA'),
 ('Logitech MX Vertical', 'usb-0000:0e:00.0-3/input2:1'),
 ('KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac',
  'usb-0000:0e:00.0-5.4.2.1/input1'),
 ('KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac',
  'usb-0000:0e:00.0-5.4.2.1/input0'),
 ('MSI MYSTIC LIGHT ', 'usb-0000:0e:00.0-10/input0'),
 ('Video Bus', 'LNXVIDEO/video/input0'),
 ('Power Button', 'LNXPWRBN/button/input0'),
 ('Power Button', 'PNP0C0C/button/input0')]

```
Replace the names in the variable `contestant_name` with the names of the input devices above. You need to use the 2nd element in the tuple, this is the physical device name such as 'usb-0000:0e:00.0-2.4/input0' instead of 'Logitech USB Optical Mouse'. The semantic name may be the same, that is you could have two logitech optical usb mice and they show up with the same name.

