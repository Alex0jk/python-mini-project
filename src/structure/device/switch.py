from .device import Device


class Switch(Device):
    def __init__(self, device_type, name, address, credentials, status, connected_devices):
        super(Switch, self).__init__(device_type, name, address, credentials, status)
        self.connected_devices = connected_devices
