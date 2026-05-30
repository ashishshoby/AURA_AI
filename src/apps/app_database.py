import psutil

APP_CACHE = {}


def build_process_cache():

    global APP_CACHE

    APP_CACHE.clear()

    for process in psutil.process_iter(['name']):

        try:

            name = process.info['name']

            if not name:
                continue

            clean_name = name.replace(".exe", "").lower()

            APP_CACHE[clean_name] = name

        except:
            pass

    print(f"Cached {len(APP_CACHE)} processes")


def get_process_name(app_name):

    app_name = app_name.lower()

    if app_name in APP_CACHE:

        return APP_CACHE[app_name]

    for key in APP_CACHE:

        if app_name in key:

            return APP_CACHE[key]

    return None