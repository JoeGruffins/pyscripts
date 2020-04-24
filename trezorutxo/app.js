var bitcoin = require('@trezor/utxo-lib')
var Buffer = require('safe-buffer').Buffer

var buf = Buffer.alloc(32)
buf[31] = 1
console.log(buf)

console.log(bitcoin.ECPair.fromPrivateKeyBuffer(buf ,bitcoin.networks.decred).getAddress())
