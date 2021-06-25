from ..structure.device.switch import Switch
from ..structure.device.pc import PC
from ..structure.device.router import Router
from ..structure.auxiliar.credential import Credential
from ..structure.program.chats import Chat

network = {
    "lobby-router": Router(
        device_type="Router",
        name="Lobby Router",
        address="lobby-router",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_devices={
            "lobby-main-switch",
            "lobby-pc",
            "lobby-info",
            "lobby-consultation",
            "lobby-employees-switch",
            "employee-1",
            "employee-2",
            "employee-3",
            "lobby-social-switch",
            "social-news",
            "social-updates",
            "social-employees",
            "internal-router"
        },
        routes={},
    ),
    "lobby-main-switch": Switch(
        device_type="Switch",
        name="Lobby Main Switch",
        address="lobby-main-switch",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_devices={"lobby-router", "lobby-pc", "lobby-info", "loby-consultation"},
    ),
    "lobby-pc": PC(
        device_type="Computer",
        name="Lobby Main PC",
        address="lobby-pc",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "lobby-info": PC(
        device_type="Computer",
        name="Lobby Info",
        address="lobby-info",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "lobby-consultation": PC(
        device_type="Computer",
        name="Lobby Consultation",
        address="lobby-consultation",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "lobby-employees-switch": Switch(
        device_type="Switch",
        name="Lobby Employees Switch",
        address="lobby-employees-switch",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_devices={"lobby-router", "employee-1", "employee-2", "employee-3"},
    ),
    "employee-1": PC(
        device_type="Computer",
        name="PC Employees 1",
        address="employee-1",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "employee-2": PC(
        device_type="Computer",
        name="PC Employees 2",
        address="employee-2",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "employee-3": PC(
        device_type="Computer",
        name="PC Employees 3",
        address="employee-3",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "lobby-social-switch": Switch(
        device_type="Switch",
        name="Lobby Social Switch",
        address="lobby-social-switch",
        credentials=Credential("admin", "admin"),
        status="Active",
        connected_devices={"lobby-router", "social-news", "social-updates", "social-employees"},
    ),
    "social-news": PC(
        device_type="Computer",
        name="BlueNetPC1",
        address="Social News",
        credentials=Credential("admin", "admin"),
        status="Inactive",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "social-updates": PC(
        device_type="Computer",
        name="Social Updates",
        address="social-updates",
        credentials=Credential("admin", "admin"),
        status="Inactive",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    ),
    "social-employees": PC(
        device_type="Computer",
        name="Social Employees",
        address="social-employees",
        credentials=Credential("admin", "admin"),
        status="Inactive",
        connected_to="lobby-router",
        programs={"chat": Chat("chat")}
    )
}
