from ..structure.device.switch import Switch
from ..structure.device.pc import PC
from ..structure.device.router import Router 

network = {
  "red" : Router(
    device_type = "Router", 
    name = "RedNetRouter", 
    address = "red", 
    credentials = "no credentials", 
    status = "Active", 
    connected_devices = { "red-s-1","red-p-2","red-p-3","black","blue","green" }, 
    routes = {} 
  ),
  "red-s-1" : Switch(
    device_type = "Switch",
    name = "RedNetSwitch",
    address = "red-s-1", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "red","red-p-2","red-p-3" }
  ),
  "red-p-2" : PC(
    device_type = "Computer",
    name = "RedNetPC1",
    address = "red-p-2",
    credentials = "no credentials",
    status = "Active",
    connected_to = "red"
  ),
  "red-p-3" : PC(
    device_type = "Computer",
    name = "RedNetPC2",
    address = "red-p-3",
    credentials = "no credentials",
    status = "Active",
    connected_to = "red"
  ),
  "black" : Router(
    device_type = "Router", 
    name = "BlackNetRouter", 
    address = "black", 
    credentials = "no credentials", 
    status = "Active", 
    connected_devices = { "black-s-1","black-p-2","black-p-3","red","blue" }, 
    routes = {} 
  ),
  "black-s-1" : Switch(
    device_type = "Switch",
    name = "BlackNetSwitch",
    address = "black-s-1", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "black","black-p-2" }
  ),
  "black-p-2" : PC(
    device_type = "Computer",
    name = "BlackNetPC1",
    address = "black-p-2",
    credentials = "no credentials",
    status = "Active",
    connected_to = "black"
  ),
  "black-p-3" : PC(
    device_type = "Computer",
    name = "BlackNetPC1",
    address = "black-p-3",
    credentials = "no credentials",
    status = "Active",
    connected_to = "black"
  ),
  "blue" : Router(
    device_type = "Router", 
    name = "BlueNetRouter", 
    address = "blue", 
    credentials = "no credentials", 
    status = "Active", 
    connected_devices = { "blue-s-1","blue-s-2","blue-s-3","blue-p-4","blue-p-5","blue-p-6","red","black" }, 
    routes = {} 
  ),
  "blue-s-1" : Switch(
    device_type = "Switch",
    name = "BlueNetSwitch1",
    address = "blue-s-1", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "blue","blue-p-4","blue-p-5" }
  ),
  "blue-s-2" : Switch(
    device_type = "Switch",
    name = "BlueNetSwitch2",
    address = "black-s-2", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "blue","blue-s-3" }
  ),
  "blue-s-3" : Switch(
    device_type = "Switch",
    name = "BlueNetSwitch3",
    address = "black-s-3", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "blue-s-2","blue-p-6" }
  ),
  "blue-p-4" : PC(
    device_type = "Computer",
    name = "BlueNetPC1",
    address = "blue-p-4",
    credentials = "no credentials",
    status = "Active",
    connected_to = "blue"
  ),
  "blue-p-5" : PC(
    device_type = "Computer",
    name = "BlueNetPC2",
    address = "blue-p-5",
    credentials = "no credentials",
    status = "Active",
    connected_to = "blue"
  ),
  "blue-p-6" : PC(
    device_type = "Computer",
    name = "BlueNetPC3",
    address = "blue-p-6",
    credentials = "no credentials",
    status = "Active",
    connected_to = "blue"
  ),
  "green" : Router(
    device_type = "Router", 
    name = "GreenNetRouter", 
    address = "green", 
    credentials = "no credentials", 
    status = "Active", 
    connected_devices = { "green-s-1","green-p-2","green-p-3","green-p-4","red" }, 
    routes = {}
  ),
  "green-s-1" : Switch(
    device_type = "Switch",
    name = "GreenNetSwitch",
    address = "green-s-1", 
    credentials = "no credentials",
    status = "Active", 
    connected_devices = { "green","green-p-2","green-p-3","green-p-4" }
  ),
  "green-p-2" : PC(
    device_type = "Computer",
    name = "GreenNetPC1",
    address = "green-p-2",
    credentials = "no credentials",
    status = "Active",
    connected_to = "green"
  ),
  "green-p-3" : PC(
    device_type = "Computer",
    name = "GreenNetPC2",
    address = "green-p-3",
    credentials = "no credentials",
    status = "Active",
    connected_to = "green"
  ),
  "green-p-4" : PC(
    device_type = "Computer",
    name = "GreenNetPC3",
    address = "green-p-4",
    credentials = "no credentials",
    status = "Active",
    connected_to = "green"
  )
}