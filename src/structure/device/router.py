from src.structure.device.device import Device
from src.utils.exceptions import RouterException


class Router(Device):
    def __init__(self, device_type, name, address, credentials, status, connected_devices, routes):
        super(Router, self).__init__(device_type, name, address, credentials, status)
        # connected devices is a set of addresses connected to the router
        self.connected_devices = connected_devices
        # routes is dict where  key: destination, value: address to lookup for destination
        self.routes = routes
        self.commands = {**self.commands, **{"routes": self.routing}}

    def routing(self, action="help", *parameters):
        output = ""

        if(action == "help"):
            output = ("To use the routing capabilities, you "
                      "have the following commands available:\n"
                      "- routes all -> This will show a list of all the routes this router has\n"
                      "- routes check [destination]-> This will show "
                      "the route to get to a destination\n"
                      "- routes create [destination] [direction] -> "
                      "This will create a new route\n"
                      "- routes delete [destination]\n"
                      "...")

        if(action == "all"):
            output = ""
            for key in self.routes:
                output = output + key + ":" + self.routes[key] + "\n"

        if(action == "check"):
            if parameters[0] in self.routes.keys():
                output = "connected by: " + self.routes[parameters[0]]
            else:
                raise RouterException(
                    "Route does not exist here"
                )

        if(action == "delete"):
            if parameters[0] in self.routes.keys():
                del self.routes[parameters[0]]
                output = parameters[0] + " successfully deleted"
            else:
                raise RouterException(
                    "Route does not exist here"
                )

        if(action == "create"):
            if parameters[0] in self.routes.keys():
                raise RouterException(
                    "Route already exist, espcify another one"
                )
            else:
                self.routes[parameters[0]] = parameters[1]
                output = parameters[0] + " connected by " + parameters[1]

        return output

    def __str__(self):
        return (
            super(Router, self).__str__()
            + "\nThis device is directly connected to the following addresses: "
            + ", ".join(self.connected_devices)
        )
