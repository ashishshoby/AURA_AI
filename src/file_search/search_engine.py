import os


def find_files(keyword, search_path="D:\\"):

    results = []

    for root, dirs, files in os.walk(search_path):

        try:

            for file in files:

                if keyword.lower() in file.lower():

                    full_path = os.path.join(
                        root,
                        file
                    )

                    results.append(full_path)

        except:
            pass

    return results