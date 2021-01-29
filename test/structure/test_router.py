import unittest
import copy

from src.structure.device.router import Router

router = Router(
    "Router",
    "Test Router 1",
    "adress-2",
    "",
    "Active",
    {"adress-1", "adress-3"},
    {"adress-5": "adress-4"},
)


class TestRouterRouting(unittest.TestCase):
    def test_routing_no_command(self):
        testing_router = copy.deepcopy(router)
        self.assertEqual(
            testing_router.routing(),
            ("To use the routing capabilities, you have the following commands available:\n"
                "- routes all -> This will show a list of all the routes this router has\n"
                "- routes check [destination]-> This will show "
                "the route to get to a destination\n"
                "- routes create [destination] [direction] -> This will create a new route\n"
                "- routes delete [destination]\n"
                "...")
        )
        self.assertEqual(testing_router.routes, {"adress-5": "adress-4"})

    def test_routing_check_all(self):
        testing_router = copy.deepcopy(router)
        self.assertEqual(testing_router.routing("all"), "adress-5:adress-4\n")
        self.assertEqual(testing_router.routes, {"adress-5": "adress-4"})

    def test_routing_check_specific(self):
        testing_router = copy.deepcopy(router)
        self.assertEqual(testing_router.routing("check", "adress-5"), "connected by: adress-4")
        self.assertEqual(testing_router.routes, {"adress-5": "adress-4"})

    def test_routing_check_specific_not_exist(self):
        testing_router = copy.deepcopy(router)
        self.assertRaises(Exception, testing_router.routing, "check", "adress-3")

    def test_routing_delete_specific(self):
        testing_router = copy.deepcopy(router)
        self.assertEqual(
            testing_router.routing("delete", "adress-5"),
            "adress-5 successfully deleted"
        )
        self.assertEqual(testing_router.routes, {})

    def test_routing_delte_specific_not_exist(self):
        testing_router = copy.deepcopy(router)
        self.assertRaises(Exception, testing_router.routing, "delete", "adress-3")

    def test_routing_create_route(self):
        testing_router = copy.deepcopy(router)
        self.assertEqual(
            testing_router.routing("create", "adress-1", "adress-2"),
            "adress-1 connected by adress-2"
        )
        self.assertDictContainsSubset({"adress-1": "adress-2"}, testing_router.routes)

    def test_routing_create_route_already_existing(self):
        testing_router = copy.deepcopy(router)
        self.assertRaises(Exception, testing_router.routing, "create", "adress-5", "adress-3")
