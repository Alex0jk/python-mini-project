class DeviceController:
  def __init__(self, devices):
      self.devices = devices #It is managed as a dictionary (address, device)
  
  def get_device(self, current_address, destination_address):
    current_device = self.devices[current_address]

    #What if where are connecting froma router?
    while True:

      if current_device.address == destination_address:
        return current_device

      elif current_device.device_type == "Computer":
        current_device = self.devices[current_device.connected_to]

      elif destination_address in current_device.connected_devices:
        return self.devices[destination_address]
      
      elif current_device.device_type == "Switch":
        raise Exception ("This devices has not been found.\n" +
                "Check if the address is correct or if it is accessible from the current Switch")

      else:
        if destination_address in current_device.routes.keys():
          current_device = self.devices[current_device.routes[destination_address]]
        else:
          raise Exception ("Route to this devices has not been found.\n" +
                  "Check if the address is correct or a route to the device exists from where you are.")
    
