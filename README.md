# Shipardy!

## Requirements
python 3.10.X

Install packages, it's recommended to use a venv

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
['Logitech Wireless Receiver Mouse',
 'Sony PLAYSTATION(R)3 Controller',
 'Sony PLAYSTATION(R)3 Controller Motion Sensors',
 'Logitech USB Optical Mouse',
 'input-remapper KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac '
 'forwarded',
 'input-remapper keyboard',
 'HDA NVidia HDMI/DP,pcm=9',
 'HDA NVidia HDMI/DP,pcm=8',
 'HDA NVidia HDMI/DP,pcm=7',
 'HDA NVidia HDMI/DP,pcm=3',
 'HD-Audio Generic HDMI/DP,pcm=9',
 'HD-Audio Generic HDMI/DP,pcm=8',
 'HD-Audio Generic HDMI/DP,pcm=7',
 'HD-Audio Generic HDMI/DP,pcm=3',
 'Logitech MX Vertical',
 'KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac',
 'KINESIS CORPORATION KB800HM Kinesis Freestyle2 for Mac',
 'MSI MYSTIC LIGHT ',
 'Video Bus',
 'Power Button',
 'Power Button']

```
Replace the names in the variable `contestant_name` with the names of the input devices above
```
