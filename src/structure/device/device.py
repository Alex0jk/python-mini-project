from src.utils.exceptions import DeviceException


class Device:
    def __init__(self, device_type, name, address, credentials, status):
        self.device_type = device_type
        self.name = name
        self.address = address
        self.credentials = credentials
        self.status = status
        self.commands = {"info": self.__str__}

    def __str__(self):
        return (
            "Welcome to "
            + self.name
            + " "
            + self.device_type
            + ", to start using type a command in the console. \n"
            + "If you have any problems type help."
            + "\n\n====DEVICE DATA====\n->Type: "
            + self.device_type
            + "\n->Name: "
            + self.name
            + "\n->Address: "
            + self.address
            + "\n->Status: "
            + self.status
        )

    def wake_up(self):
        pass

    def login(self):
        user = input("Device username: ")
        password = input("Device password: ")
        if self.credentials.check_correct_credentials(user, password):
            return True
        else:
            raise DeviceException(
                "Incorrect credentials, you may not access this device"
            )
