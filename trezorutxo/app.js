var bitcoin = require('@trezor/utxo-lib')
var Buffer = require('safe-buffer').Buffer

var buf = Buffer.alloc(32)
buf[31] = 1
console.log(buf)
pair = bitcoin.ECPair.fromPrivateKeyBuffer(buf, bitcoin.networks.decred)
console.log(pair.getPublicKeyBuffer())
address = pair.getAddress()
console.log(address)
checked = bitcoin.address.fromBase58Check(address, bitcoin.networks.decred.coin)
console.log(checked)
checked = bitcoin.address.fromBase58Check("DsmcYVbP1Nmag2H4AS17UTvmWXmGeA7nLDx", bitcoin.networks.decred.coin)
console.log(checked)
