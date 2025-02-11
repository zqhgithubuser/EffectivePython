import sys


def do_processing():
    pass


def main(argv):
    while True:
        try:
            do_processing()
        except Exception as e:
            print("Error:", type(e), e)
        except KeyboardInterrupt:
            found = input("Terminate? [y/n]: ")
            if found == "y":
                raise  # Propagate the error


if __name__ == "__main__":
    sys.exit(main(sys.argv))
