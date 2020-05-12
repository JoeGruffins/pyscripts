#!/usr/bin/env python3
from decred.crypto import crypto
from decred.dcr import addrlib
from decred.dcr.nets import mainnet, testnet, simnet
from decred.util.encode import ByteArray
from base58 import b58decode, b58encode


def main():
    ba = ByteArray(1, length=32)
    priv = crypto.privKeyFromBytes(ba)
    pub = priv.pub
    pkh = crypto.hash160(pub.serializeCompressed().b)
    addrPKH = addrlib.AddressPubKeyHash(pkh, mainnet)
    print([x for x in ba])
    print(pub.serializeCompressed().b.hex())
    print(addrPKH.string())
    h = ByteArray("751e76e8199196d454941c45d1b3a323f1433bd6")
    addrPKH = addrlib.AddressPubKeyHash(h, mainnet)
    print(addrPKH.string())
    addrPKH = addrlib.AddressPubKeyHash(h, testnet)
    print(addrPKH.string())
    addrPKH = addrlib.AddressPubKeyHash(h, simnet)
    print(addrPKH.string())


main()
