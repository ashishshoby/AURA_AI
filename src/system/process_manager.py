import psutil


def get_top_cpu_processes(limit=10):

    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name', 'cpu_percent']
    ):

        try:

            processes.append({
                "name": proc.info["name"],
                "cpu": proc.info["cpu_percent"]
            })

        except:
            pass

    processes.sort(
        key=lambda x: x["cpu"],
        reverse=True
    )

    return processes[:limit]


def get_top_ram_processes(limit=10):

    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name', 'memory_percent']
    ):

        try:

            processes.append({
                "name": proc.info["name"],
                "ram": round(
                    proc.info["memory_percent"],
                    2
                )
            })

        except:
            pass

    processes.sort(
        key=lambda x: x["ram"],
        reverse=True
    )

    return processes[:limit]


def kill_process(name):

    killed = False

    for proc in psutil.process_iter(
        ['name']
    ):

        try:

            if proc.info['name']:

                if name.lower() in proc.info[
                    'name'
                ].lower():

                    proc.kill()

                    killed = True

        except:
            pass

    return killed