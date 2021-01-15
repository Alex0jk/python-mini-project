import unittest

from .device_controller import DeviceController
from ..structure.device.pc import PC
from ..structure.device.router import Router 


class TestDeviceController(unittest.TestCase):
  # test connect from switch and connect from router
  def test_get_device_existing(self):
    test_controller = DeviceController({
      "adress-1" : PC("Computer", "Test Computer 1", "adress-1", "", "Active", "adress-2"),
      "adress-2" : Router("Router", "Test Router 1", "adress-2", "", "Active", { "adress-1","adress-3" }, {"adress-5":"adress-4"} ),
      "adress-3" : PC("Computer", "Test Computer 2", "adress-3", "", "Active", "adress-2"),
    })

    self.assertEqual(test_controller.get_device("adress-1","adress-3"), test_controller.devices["adress-3"])

  def test_get_device_not_existing(self):
    test_controller = DeviceController({
      "adress-1" : PC("Computer", "Test Computer 1", "adress-1", "", "Active", "adress-2"),
      "adress-2" : Router("Router", "Test Router 1", "adress-2", "", "Active", { "adress-1","adress-3" }, {"adress-5":"adress-4"} ),
      "adress-3" : PC("Computer", "Test Computer 2", "adress-3", "", "Active", "adress-2"),
    })
    self.assertRaises(Exception, test_controller.get_device, "adress-1","adress-4")

  def test_get_device_another_network(self):
    test_controller = DeviceController({
      "adress-1" : PC("Computer", "Test Computer 1", "adress-1", "", "Active", "adress-2"),
      "adress-2" : Router("Router", "Test Router 1", "adress-2", "", "Active", { "adress-1","adress-3","adress-4" }, {"adress-5":"adress-4"} ),
      "adress-3" : PC("Computer", "Test Computer 2", "adress-3", "", "Active", "adress-2"),
      "adress-4" : Router("Router", "Test Router 2", "adress-4", "", "Active", { "adress-2","adress-5" }, {"adress-1":"adress-2"} ),
      "adress-5" : PC("Computer", "Test Computer 3", "adress-5", "", "Active", "adress-4"),
    })

    self.assertEqual(test_controller.get_device("adress-1","adress-5"), test_controller.devices["adress-5"])

  def test_get_device_same(self):
    test_controller = DeviceController({
      "adress-1" : PC("Computer", "Test Computer 1", "adress-1", "", "Active", "adress-2"),
      "adress-2" : Router("Router", "Test Router 1", "adress-2", "", "Active", { "adress-1","adress-3" }, {"adress-5":"adress-4"} ),
      "adress-3" : PC("Computer", "Test Computer 2", "adress-3", "", "Active", "adress-2"),
    })

    self.assertEqual(test_controller.get_device("adress-1","adress-1"), test_controller.devices["adress-1"])

  def test_get_device_from_router(self):
    test_controller = DeviceController({
      "adress-1" : PC("Computer", "Test Computer 1", "adress-1", "", "Active", "adress-2"),
      "adress-2" : Router("Router", "Test Router 1", "adress-2", "", "Active", { "adress-1","adress-3" }, {"adress-5":"adress-4"} ),
      "adress-3" : PC("Computer", "Test Computer 2", "adress-3", "", "Active", "adress-2"),
    })

    self.assertEqual(test_controller.get_device("adress-2","adress-3"), test_controller.devices["adress-3"])

if __name__ == '__main__':
    unittest.main()