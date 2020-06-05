import os
from collections import Counter
from pprint import pprint

__all__ = ['all_files', 'file_types', "find_files_by_type"]


def all_files(folder):
    return ((path, filename) for path, dirs, files in os.walk(folder) for filename in files)


def file_types(folder=""):
    c = Counter(os.path.splitext(name)[1] for path, name in all_files(folder))
    pprint(c.most_common())
    return c.most_common()


def find_files_by_type(folder="", ext=""):
    c = Counter((path, os.path.splitext(name)[1]) for path, name in all_files(folder) if name.endswith(ext))
    pprint(c.most_common())
