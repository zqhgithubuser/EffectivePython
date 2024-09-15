pictures = {}
path = "profile_0001.jpg"


def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f"Failed to open path {profile_path}")
        raise


class Pictures(dict):

    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
