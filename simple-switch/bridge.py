import subprocess

def create(name: str) -> None:
    subprocess.run(["brctl", "addbr", name], check=True)

def include(br: str, iface: str) -> None:
    subprocess.run(["brctl", "addif", br, iface], check=True)

def stp(br: str, status: str) -> None:
    subprocess.run(["brctl", "stp", br, status], check=True)
