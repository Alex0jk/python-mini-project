from .controller.game_controller import Game_Controller

game = Game_Controller()

if __name__ == "__main__":
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

        game.execute(command, executed_method)
