from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def _get_volume():

    device = AudioUtilities.GetSpeakers()

    interface = device.EndpointVolume

    return cast(
        interface,
        POINTER(IAudioEndpointVolume)
    )


def volume_up():

    volume = _get_volume()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(
        min(1.0, current + 0.1),
        None
    )

    return "Volume increased."


def volume_down():

    volume = _get_volume()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(
        max(0.0, current - 0.1),
        None
    )

    return "Volume decreased."


def mute():

    volume = _get_volume()

    volume.SetMute(True, None)

    return "Audio muted."


def unmute():

    volume = _get_volume()

    volume.SetMute(False, None)

    return "Audio unmuted."


def set_volume(percent):

    volume = _get_volume()

    percent = max(
        0,
        min(100, int(percent))
    )

    volume.SetMasterVolumeLevelScalar(
        percent / 100,
        None
    )

    return f"Volume set to {percent} percent."