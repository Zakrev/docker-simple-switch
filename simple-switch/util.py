import subprocess

def updown(iface: str, state: str) -> None:
    subprocess.run(["ip", "link", "set", state, iface], check=True)

def disable_ipv6() -> None:
    subprocess.run(["sysctl", "-w", "net.ipv6.conf.all.disable_ipv6=1"], check=True)
