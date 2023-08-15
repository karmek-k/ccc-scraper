from sys import stderr


def die(text, status=1):
    """Prints `text` to stderr and exits with `status`"""

    print(text, file=stderr)
    exit(status)

