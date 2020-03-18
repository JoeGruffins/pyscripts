package main

import (
	"encoding/hex"
	"fmt"
	"github.com/decred/dcrd/crypto/blake256"
)

func main() {
	h := "17446563726564205369676e6564204d6573736167653a0a0a31353834343231313833"
	b, err := hex.DecodeString(h)
	if err != nil {
		panic(err)
	}
	hash := blake256.Sum256(b)
	fmt.Println(hex.EncodeToString(hash[:]))
}
