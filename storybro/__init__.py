"""A community fork of AI Dungeon 2"""

__version__ = "0.1.0"

import sys

del sys.modules['readline']

from .cli import ep

def main():
    ep()
