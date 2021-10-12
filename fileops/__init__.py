"""
Simple package to do file operations easier
Read https://pypi.org/project/simple-file-ops/ for more info
"""

from .jsonops import read_json, write_json, get_json_key, load, loads, dump, dumps
from .textfiles import read, readlines, write, append

__version__ = "0.1.2"
__author__ = "Cube Riser"
