from src.structure.device.device import Device


class PC(Device):
    def __init__(self, device_type, name, address, credentials, status, connected_to, programs):
        super(PC, self).__init__(device_type, name, address, credentials, status)
        self.connected_to = connected_to
        self.programs = programs
        self.commands = {**self.commands, **{k: v.execute for k, v in self.programs.items()}}

    def __str__(self):
        return (
            super(PC, self).__str__()
            + "\nThis device is directly connected to the following address: "
            + self.connected_to
        )
