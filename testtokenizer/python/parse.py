#!/usr/bin/env python3
from decred.dcr import txscript, nets
from decred.crypto import crypto
from base58 import b58decode
from decred.util.encode import ByteArray


def main():
    script = ByteArray("512103af3c24d005ca8b755e7167617f3a5b4c60a65f8318a7fcd1b0cacb1abd2a97fc21027b81bc16954e28adb832248140eb58bedb6078ae5f4dabf21fde5a8ab7135cb652ae")
    print(crypto.hash160(script.bytes()).hex())

    _, addrs, _ = txscript.extractPkScriptAddrs(0, script, nets.testnet)
    for addr in addrs:
        print("addr", addr.string())


def parse(b):
    data = None
    t = txscript.ScriptTokenizer(0, b)
    while t.next():
        d = t.data()
        if d:
            data = d
            print(data.hex())
    if t.err is not None:
        raise Exception(t.err)
    return data


main()
