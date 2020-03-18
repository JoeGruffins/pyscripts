package main

import (
	"encoding/hex"
	"fmt"
	"github.com/decred/dcrd/dcrec/secp256k1/v3"
)

func main() {
	h, err := hex.DecodeString("577811a230cf0c352a01bfa044287e9f8b630dacd796e375515377126b8fe046")
	if err != nil {
		panic(err)
	}
	//hash, err := hex.DecodeString("a5e4d4d0c3b77a98c5227d6c3255a29428a106aac5e5e2c3a6d7782396e667c4")
	hash, err := hex.DecodeString("62bde5b4c2b855fc32de5586e9c849457453d2ec2aa2f1a539258766d9008295")
	if err != nil {
		panic(err)
	}
	key := secp256k1.PrivKeyFromBytes(h)
	sig := secp256k1.SignCompact(key, hash, true)
	fmt.Println(hex.EncodeToString(sig))
}
