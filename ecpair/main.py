#!/usr/bin/env python3
from decred.crypto import crypto
from decred.dcr import addrlib
from decred.dcr.nets import mainnet
from decred.util.encode import ByteArray


def main():
    ba = ByteArray(1, length=32)
    priv = crypto.privKeyFromBytes(ba)
    pub = priv.pub
    pkh = crypto.hash160(pub.serializeCompressed().b)
    addrPKH = addrlib.AddressPubKeyHash(pkh, mainnet)
    print([x for x in ba])
    print(addrPKH.string())


main()
