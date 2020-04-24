package main

import (
	"encoding/hex"
	"fmt"
	"github.com/decred/dcrd/crypto/blake256"
)

func main() {
	b := make([]byte, 32)
	hash := blake256.Sum256(b)
	fmt.Println(b)
	fmt.Println(hex.EncodeToString(hash[:]))
}
