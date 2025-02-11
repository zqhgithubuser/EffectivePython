import sys


def do_processing(handle):
    pass


def main(argv):
    data_path = argv[1]
    handle = open(data_path, "w+")

    try:
        while True:
            try:
                do_processing(handle)
            except Exception as e:
                print("Error:", type(e), e)
    finally:
        print("Cleaning up finally")
        handle.flush()
        handle.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
