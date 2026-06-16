import os


def shutdown_pc():

    os.system(
        "shutdown /s /t 0"
    )

    return "Shutting down computer."


def restart_pc():

    os.system(
        "shutdown /r /t 0"
    )

    return "Restarting computer."


def lock_pc():

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return "Locking computer."


def sleep_pc():

    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )

    return "Putting computer to sleep."