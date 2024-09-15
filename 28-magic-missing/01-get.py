pictures = {}
path = "profile_0001.jpg"

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f"Failed to open path {path}")
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()
