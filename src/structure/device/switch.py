from .device import Device


class Switch(Device):
    def __init__(self, device_type, name, address, credentials, status, connected_devices):
        super(Switch, self).__init__(device_type, name, address, credentials, status)
        self.connected_devices = connected_devices

    def __str__(self):
        return (
            super(Switch, self).__str__()
            + "\nThis device is directly connected to the following addresses: "
            + ", ".join(self.connected_devices)
        )
