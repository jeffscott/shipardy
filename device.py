from evdev import InputDevice, list_devices
from pprint import pprint as pp


class DeviceManager:

    """
    This class finds the input devices connected to a machine and displays the info. Contestants are assigned
    to devices via dictionary entry.
    """
    def __init__(self) -> None:
        
        self.devices = {}
        self.device_list = [InputDevice(path) for path in list_devices()]
        self.devices= {device.name: {"input_device": device, "contestant_name": None} for device in self.device_list}
        self.contestant_devices = None # Used to pass to select module for I/O disambiguation


    def assign_contestant(self, contestant_name: str, device_name: str) -> None:

        """
        Assign a device number to the contestant name. Update the list of active contestant devices.
        """
        try:
            self.devices[device_name]['contestant_name'] = contestant_name
        except KeyError:
            print(f"No device name: {device_name}")

        self. _update_contestant_device_list()

    def remove_contestant(self, contestant_name: str, device_name: str) -> None:
        
        self.devices[device_name]['contestant_name'] = None
        self._update_contestant_device_list()


    def _update_contestant_device_list(self):

        self.contestant_devices = [device['input_device'] for name, device in self.devices.items() if device['contestant_name'] is not None]


    def get_contestant_devices(self) -> list[InputDevice]:

        """
        Return a list of currently selected InputDevices for all contestants 
        """
        
        return self.contestant_devices
        
    def print_devices(self) -> None:

        for name, device in self.devices.items():
            print(device)
            print(f"  DeviceName: {name}")
            print(f"  DeviceType: {device['input_device']}")
            print(f"  DeviceCont: {device['contestant_name']}\n")

    def list_available_devices(self) -> None:

        pp([device.name for device in self.device_list])

    def print_contestants(self) -> None:

        if not self.contestant_devices:
            print('No Current Contestants!')
            return None

        print('Current contestants')
        for name, device in self.devices.items():
            if device['contestant_name'] is not None:
                print(f"{device['contestant_name']}: {name}")