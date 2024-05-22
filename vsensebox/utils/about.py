# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from .commontools import joinFPathFull, getGlobalRootDir

def getVersionString():
    """
    :meta private:
    """
    version_py = joinFPathFull(getGlobalRootDir(), '__init__.py')
    with open(version_py) as version_file:
        for line in version_file.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            msg = "Unable to find version string."
            raise RuntimeError(msg)

def github():
    """
    :meta private:
    """
    import webbrowser
    webbrowser.open('https://github.com/numediart/vsensebox.git')

def docs():
    """
    :meta private:
    """
    import webbrowser
    webbrowser.open('https://numediart.github.io/vsensebox')
