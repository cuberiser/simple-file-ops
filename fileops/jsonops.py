import json


def read_json(filepath: str):
    """
    Reads a json file, and returns the data as a dict or list
    """
    if type(filepath) != str:
        raise TypeError(
            f"File path needs to be of type string not type {type(filepath)}"
        )
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def load(filepath: str):
    """
    Alias for fileops.jsonops.read_json
    """
    return read_json(filepath)


def write_json(filepath: str, data, indent: int = 4):
    """
    Writes a json file with the given data and indent, or creates one if it doesn't exist
    """
    if type(filepath) != str:
        raise TypeError(
            f"Filepath needs to be of type string not of type {type(filepath)}"
        )
    if type(data) != list and type(data) != dict:
        raise TypeError(f"data needs to be of type dict or list not {type(data)}")
    if type(indent) != int:
        raise TypeError(f"indent needs to be of type int not {type(indent)}")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=indent)


def dump(filepath: str, data, indent: int = 4):
    """
    Pointer function to write_json
    """
    return write_json(filepath, data, indent)


def get_json_key(filepath: str, keyname: str):
    """
    Gets a json file key from specified filepath and keyname
    """
    if type(filepath) != str:
        raise TypeError("filepath needs to be of type string")
    if type(keyname) != str:
        raise TypeError(f"Keyname needs to be of type string not type {type(keyname)}")
    with open(filepath, "r") as f:
        data = json.load(f)
    return data[keyname]


def get_key(filepath, keyname):
    """
    pointer for get_json_key
    """
    return get_json_key(filepath, keyname)


def dumps(data, indent: int = 4):
    """
    Alias for json.dumps.
    """

    if type(data) != list and type(data) != dict:
        raise TypeError(f"data needs to be of type dict or list not {type(data)}")

    return json.dumps(data, indent=indent)


def loads(loadstr):
    """
    alias for json.loads.
    """
    if type(loadstr) != str:
        raise TypeError(
            f"loadable string needs to be of type string not {type(loadstr)}"
        )
    return json.loads(loadstr)
