import functools
import sys
from ..utils.utility_classes import Singleton
from ..data.network import network
from ..controller.device_controller import DeviceController


class Game_Controller():
    def __init__(self):
        self.device_controller = DeviceController(network)
        self.current_device = network["red-p-3"]
        self.commands = {
            "connect": self.connect,
            "where_am_i": self.print_current_device,
            "exit": self.exit_game
        }

    def execute(self, command_name, command_to_execute):
        try:
            if command_name in self.commands.keys():
                eval(command_to_execute, {'__builtins__': None}, self.commands)
            else:
                print(
                    eval(command_to_execute, {'__builtins__': None}, self.current_device.commands)
                )

        except Exception as error:
            print("Command invalid " + str(error))

    def connect(self, destination):
        print(destination)
        try:
            self.current_device = self.device_controller.get_device(
                self.current_device.address, destination
            )
        except Exception as error:
            print(error)

    def print_current_device(self):
        print(self.current_device)

    def exit_game(self):
        sys.exit()

    __metaclass__ = Singleton
