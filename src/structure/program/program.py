from src.utils.input_processing import input_to_command_transform


class Program:
    def __init__(self, name):
        self.name = name
        self.commands = {"help": self.help}

    def execute(self):
        while True:
            command_tuple = input_to_command_transform("Command for " + self.name + ": ")
            if command_tuple[0] == "exit":
                break
            else:
                print(eval(command_tuple[1], {'__builtins__': None}, self.commands))

        return "Thanks for using " + self.name

    def help(self):
        return ("Welcom to " + self.name + ", Here is a list of commands you can use\n\n"
                "exit -> exits from the program\n"
                "help -> a list of commands you can use\n")
