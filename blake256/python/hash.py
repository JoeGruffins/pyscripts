#!/usr/bin/env python3

from blake256.blake256 import blake_hash


def main():
    h = bytes(32)
    print(h)
    print(blake_hash(h).hex())


main()
