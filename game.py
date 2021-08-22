from src.controller.game_controller import Game_Controller
from src.utils.input_processing import input_to_command_transform

game = Game_Controller()

if __name__ == "__main__":
    while True:
        game.execute(input_to_command_transform("What is your next command: "))