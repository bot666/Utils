import difflib
import os
import platform
import re
import sys

__all__ = ['pwd', 'ls', 'find_str', 'diff']


def pwd():
    print(os.getcwd())


def ls(dir_name=''):
    if platform.system() in ("Darwin", "Linux"):
        return os.system(f'ls {dir_name}')
    elif platform.system() == 'Windows':
        return os.system(f'dir {dir_name}')


def find_str(strpattern="", file=""):
    if os.path.isfile(file):
        if file.endswith('.pyc'):
            return
        pattern = f'^{strpattern}.|.{strpattern}.|.{strpattern}$'
        with open(file) as target:
            print(f"in file {file}")
            lines = target.readlines()
            for line in zip(range(1, len(lines), 1), lines):
                if re.search(pattern, line[1]):
                    sys.stdout.writelines(f"    on line {line[0]} >> {line[1]}")
    elif os.path.isdir(file):
        inside = os.listdir(file)
        os.chdir(file)
        for i in inside:
            find_str(strpattern, i)
        os.chdir("..")
    else:
        raise Exception("No idea what it is")


def diff(fromfile=None, tofile=None):
    if os.path.isdir(fromfile or tofile):
        return
    fromlines = open(fromfile).readlines()
    tolines = open(tofile).readlines()
    diff = difflib.context_diff(fromlines, tolines, fromfile, tofile)
    sys.stdout.writelines(diff)
