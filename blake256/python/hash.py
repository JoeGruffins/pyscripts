#!/usr/bin/env python3

from blake256.blake256 import blake_hash
from decred.util.encode import ByteArray


def main():
    h = ByteArray("17446563726564205369676e6564204d6573736167653a0a0a31353834343231313833")
    bHashed = ByteArray(blake_hash(h.bytes()), length=32)
    print(bHashed.hex())


main()
