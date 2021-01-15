from .controller.game_controller import Game_Controller
from .controller.device_controller import DeviceController
from .data.network import network

game = Game_Controller(
  DeviceController(network),
  network["red-p-3"]
)

if __name__ == "__main__":
  game.start()