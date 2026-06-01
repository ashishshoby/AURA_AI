import psutil
import shutil
import socket


def get_battery_status():

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is unavailable."

    percent = battery.percent

    charging = battery.power_plugged

    if charging:
        return f"Battery is at {percent} percent and charging."

    return f"Battery is at {percent} percent."


def get_cpu_usage():

    usage = psutil.cpu_percent(interval=1)

    return f"CPU usage is {usage} percent."


def get_ram_usage():

    ram = psutil.virtual_memory()

    return (
        f"RAM usage is {ram.percent} percent. "
        f"{round(ram.used / (1024**3),1)} GB used out of "
        f"{round(ram.total / (1024**3),1)} GB."
    )


def get_disk_space():

    disk = shutil.disk_usage("C:\\")

    free_gb = round(disk.free / (1024**3), 1)

    total_gb = round(disk.total / (1024**3), 1)

    return (
        f"Drive C has {free_gb} GB free "
        f"out of {total_gb} GB."
    )


def get_wifi_status():

    try:

        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3
        )

        return "Internet connection is active."

    except:

        return "No internet connection detected."