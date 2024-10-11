import os

def __config_get_iface(config: dict, name: str) -> dict:
    if config.get("iface") == None:
        config["iface"] = dict()
        eth = None
    else:
        eth = config["iface"].get(name)
    if eth == None:
        eth = dict()
        config["iface"][name] = eth
    return eth

def __config_get_vlan(config: dict, id: int) -> dict:
    if config.get("vlan") == None:
        config["vlan"] = dict()
        vlan = None
    else:
        vlan = config["vlan"].get(id)
    if vlan == None:
        vlan = dict()
        vlan["members"] = list()
        config["vlan"][id] = vlan
    return vlan

def __parse_vlan(config: dict, key_val: str, val: str) -> None:
    for vlan_id in val.split(" "):
        vlan = __config_get_vlan(config, int(vlan_id))
        vlan["members"].append(key_val)

def __parse_native(config: dict, key_val: str, val: str) -> None:
    iface = __config_get_iface(config, key_val)
    iface["native"] = int(val)

__keys = {
    "ALLOW_VLAN": __parse_vlan,
    "NATIVE_VLAN": __parse_native,
}

def parse_from_env() -> dict:
    config = dict()
    for var in os.environ:
        if not var.startswith("SSWITCH_"):
            continue
        idx = var.find("__")
        if idx == -1:
            continue
        key = var[len("SSWITCH_"): idx]
        idx += 2
        key_val = var[idx:]
        __keys[key](config, key_val, os.environ[var])
    return config
