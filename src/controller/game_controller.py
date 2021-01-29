import functools


class Game_Controller:
    def __init__(self, device_controller, current_device):
        self.device_controller = device_controller
        self.current_device = current_device
        self.commands = {"connect": self.connect, "where_am_i": self.print_current_device}

    def start(self):  # this needs a refactor for more straight forward execution
        while True:
            user_input = input("What is your next command: ")

            user_input_divide = user_input.split()
            command = user_input_divide[0]
            arguments = ""

            for arg in user_input_divide[1:]:
                arguments = arguments + '"' + arg + '",'

            if arguments:
                executed_method = command + "(" + arguments[:-1] + ")"
            else:
                executed_method = command + "()"

            try:
                if command in self.commands.keys():
                    eval(executed_method, {'__builtins__': None}, self.commands)
                else:
                    print(
                        eval(executed_method, {'__builtins__': None}, self.current_device.programs)
                    )

            except Exception as error:
                print("Command invalid " + str(error))

            if user_input == "exit":
                print("session end")
                return

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
