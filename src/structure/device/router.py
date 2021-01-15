from .device import Device

class Router(Device):
    def __init__(self, device_type, name, address, credentials, status, connected_devices, routes):
        super(Router, self).__init__(device_type, name, address, credentials, status)
        self.connected_devices = connected_devices
        self.routes = routes