import subprocess
from . import bridge, util

class Vlan():
    def __init__(self, id: int) -> None:
        self._id = id
        self._name = "vlan." + str(id)
        self._allowed = list()
        self._native = list()
        bridge.create(self._name)
        bridge.stp(self._name, "on")
        util.updown(self._name, "up")

    def allowed(self, iface: str) -> None:
        print("APPLYING VLAN", self._id, "ON INTERFACE", iface)
        name = "{}.{}".format(iface, self._id)
        self.__subiface(iface, name)
        bridge.include(self._name, name)
        util.updown(name, "up")
        self._allowed.append(iface)

    def native(self, iface: str) -> None:
        print("APPLYING NATIVE VLAN", self._id, "ON INTERFACE", iface)
        util.updown(iface, "down")
        bridge.include(self._name, iface)
        util.updown(iface, "up")
        self._native.append(iface)

    def __subiface(self, iface: str, name: str) -> None:
        subprocess.run(["ip", "link", "add", "link", iface, "name", name,
                        "type", "vlan", "id", str(self._id)], check=True)

    def __str__(self) -> str:
        allowed = ""
        for iface in self._allowed:
            allowed += iface + " "
        native = ""
        for iface in self._native:
            native += iface + " "
        return "VLAN: {}\n\tBRIDGE: {}\n\tALLOWED: {}\n\tNATIVE: {}".format(
            self._id, self._name, allowed, native)
