import os
from datetime import datetime
import pyautogui


def take_screenshot():

    try:

        save_dir = os.path.join(
            os.path.expanduser("~"),
            "Pictures",
            "Aura Screenshots"
        )

        os.makedirs(
            save_dir,
            exist_ok=True
        )

        filename = (
            "screenshot_"
            + datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".png"
        )

        filepath = os.path.join(
            save_dir,
            filename
        )

        image = pyautogui.screenshot()

        image.save(filepath)

        print("Saved Screenshot:", filepath)

        return (
            "Screenshot saved in Pictures Aura Screenshots folder."
        )

    except Exception as e:

        print("Screenshot Error:", e)

        return (
            "Failed to save screenshot."
        )