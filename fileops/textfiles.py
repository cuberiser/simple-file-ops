def readlines(filepath: str):
    """
    Easy way to get list of lines of the file given
    """
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines


def read(filepath: str):
    """
    Easy way to get data of the file given
    """
    with open(filepath, "r") as f:
        data = f.read()
    return data


def write(filepath: str, data: str):
    """
    Easy way to write the data of the file given
    """
    with open(filepath, "w") as f:
        f.write(data)


def append(filepath: str, data: str):
    """
    Easy way to append data the file given
    """
    with open(filepath, "a") as f:
        f.write(data)
