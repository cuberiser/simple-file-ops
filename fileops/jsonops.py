import json


def read_json(filepath: str):
    """
    Reads a json file, and returns the data as a dict or list
    """
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def load(filepath: str):
    """
    Alias for read_json
    """
    return read_json(filepath)


def write_json(filepath: str, data, indent: int = 4, **kwargs):
    """
    Writes a json file with the given data and indent, or creates one if it doesn't exist
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=indent, **kwargs)


def dump(filepath: str, data, indent: int = 4, **kwargs):
    """
    Alias for fileops.jsonops.write_json
    """
    return write_json(filepath, data, indent, **kwargs)


def get_json_key(filepath: str, keyname: str):
    """
    Gets a json file key from specified filepath and keyname
    """
    with open(filepath, "r") as f:
        data: dict = json.load(f)
    return data.get(keyname)


def get_key(filepath, keyname):
    """
    Pointer to get_json_key
    """
    return get_json_key(filepath, keyname)


def dumps(data, indent: int = 4, **kwargs):
    """
    Dumps json serializable data to a string
    """

    return json.dumps(data, indent=indent, **kwargs)


def loads(loadstr):
    """
    Loads json data from a string
    """
    return json.loads(loadstr)
