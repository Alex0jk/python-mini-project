import functools
import sys
from src.utils.utility_classes import Singleton
from src.utils.exceptions import DeviceException, DeviceSearchException, RouterException
from src.data.network import network
from src.controller.device_controller import DevicesController


class Game_Controller():
    def __init__(self):
        self.device_controller = DevicesController(network)
        self.current_device = network["lobby-pc"]
        self.commands = {
            "connect": self.connect,
            "where_am_i": self.print_current_device,
            "exit": self.exit_game
        }

    def execute(self, command_tuple):
        try:
            if command_tuple[0] in self.commands.keys():
                print(eval(command_tuple[1], {'__builtins__': None}, self.commands))
            else:
                print(
                    eval(command_tuple[1], {'__builtins__': None}, self.current_device.commands)
                )

        except (DeviceException, DeviceSearchException, RouterException) as error:
            print("Erro during request:\n" + str(error))

        except TypeError as error:
            print("Command invalid" + str(error))

    def connect(self, destination):
        searched_device = self.device_controller.get_device(
            self.current_device.address, destination
        )
        searched_device.login()

        #TODO - Do not ask for credentials if connected to the same device

        self.current_device = searched_device
        return self.current_device.__str__()

    def print_current_device(self):
        return self.current_device

    def exit_game(self):
        sys.exit()

    __metaclass__ = Singleton
