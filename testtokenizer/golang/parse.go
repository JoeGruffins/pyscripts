package main

import (
	"encoding/hex"
	"fmt"
	"github.com/decred/dcrd/txscript"
)

func main() {
	h := "512103af3c24d005ca8b755e7167617f3a5b4c60a65f8318a7fcd1b0cacb1abd2a97fc21027b81bc16954e28adb832248140eb58bedb6078ae5f4dabf21fde5a8ab7135cb652ae"
	//h := "304402200aa179068a83843de4f92cd629043b1769b678370a95c2db712a087c07a1e52d0220571112746359dad1ef5fc65096cee4131cfe507bb9b9ab7ea41da21bc18d71b8011976a914000000000000000000000000000000000000000088ac"
	b, err := hex.DecodeString(h)
	if err != nil {
		panic(err)
	}
	fmt.Println(b)
	firstPass := parse(b)
	fmt.Println(firstPass)
}

func parse(b []byte) []byte {
	var data []byte
	t := txscript.MakeScriptTokenizer(0, b)

	for t.Next() {
		data = t.Data()
		fmt.Println(data)
	}
	if t.Err() != nil {
		panic(t.Err())
	}
	return data
}
