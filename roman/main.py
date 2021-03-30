# -*- coding: utf-8 -*-

"""
Main module

Copyright © 2021 Roman Clavier

Python describing
"""

import roman.base64 as base64


def main():
    """
    The main function
    """
    initial = "ABCDE"
    codex = base64.encode(initial)
    print(f"\nEncode to   base64: {initial} -> {codex}\n")

    # codex = codex.replace('=', '')
    initial = base64.decode(codex)
    print(f"\nDecode from base64: {codex} -> {initial}\n")


if __name__ == "__main__":
    main()
