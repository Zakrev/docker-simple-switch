import pprint
import time
from . import config, vlan, util

if __name__ == '__main__':
    cfg = config.parse_from_env()
    print("CONFIG:")
    pprint.pprint(cfg)
    vlans = dict()
    vlans_cfg = cfg.get("vlan")
    if vlans_cfg != None: 
        for vlan_id in vlans_cfg.keys():
            vl = vlan.Vlan(vlan_id)
            vlans[vlan_id] = vl
            for iface in vlans_cfg[vlan_id]["members"]:
                vl.allowed(iface)
    iface_cfg = cfg.get("iface")
    if iface_cfg != None:
        for iface in iface_cfg.keys():
            native = iface_cfg[iface].get("native")
            if native == None:
                continue
            vl = vlans.get(native)
            if vl == None:
                vl = vlan.Vlan(native)
                vlans[native] = vl
            vl.native(iface)
    util.disable_ipv6()
    print("APPLIED:")
    for vlan_id in vlans.keys():
        print(vlans[vlan_id])
    while True:
        time.sleep(1)
