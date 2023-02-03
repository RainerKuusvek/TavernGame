"""Text wrapper and formatter"""
import argparse
import os
import sys
from collections import deque
from tempfile import NamedTemporaryFile
from typing import List


def wrap(filename: str, linewidth: int) -> int:
    """Main function"""
    if not os.path.isfile(filename):
        print(f"Error: file '{filename}' not found")
        return 1

    with open(filename) as infile:
        lines = infile.read().splitlines()

    formatted_lines: List[str] = []
    for line in lines:
        if len(line) <= linewidth:
            formatted_lines.append(line + '\n')
            continue

        indent = 0
        for char in line:
            if char != ' ':
                break
            indent += 1
        newline = ' ' * indent

        words = deque(line.split())

        first_word = True
        while words:
            word = words[0]
            if first_word:
                newline += word
                words.popleft()
                first_word = False
                continue

            if len(newline) + 1 + len(word) <= linewidth:
                newline = newline + ' ' + word
                words.popleft()

            else:
                formatted_lines.append(newline + '\n')
                newline = ''
                first_word = True

        if newline:
            formatted_lines.append(newline + '\n')

    with NamedTemporaryFile('r+', dir='.', delete=False) as tempfile:
        tempfile.writelines(formatted_lines)

    os.rename(tempfile.name, filename)

    return 0


def cli() -> None:
    """Commandline interface"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file name')
    parser.add_argument('-w', '--width', metavar='N',
                        help='line width', type=int, default=72)

    args = parser.parse_args()

    sys.exit(wrap(args.filename, args.width))
