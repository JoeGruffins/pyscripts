#!/usr/bin/env python3
from decred.dcr import txscript
from decred.util.encode import ByteArray


def main():
    privKey = ByteArray("577811a230cf0c352a01bfa044287e9f8b630dacd796e375515377126b8fe046")
    #msg = ByteArray("a5e4d4d0c3b77a98c5227d6c3255a29428a106aac5e5e2c3a6d7782396e667c4")
    msg = ByteArray("62bde5b4c2b855fc32de5586e9c849457453d2ec2aa2f1a539258766d9008295")
    sig = txscript.signCompact(privKey, msg, True)
    print(sig.hex())

main()
