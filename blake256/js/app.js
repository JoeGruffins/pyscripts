var blake2b_ = require('blake2b')
var blake_ = require('blake-hash')
var Buffer = require('safe-buffer').Buffer

function blake2b(buffer) {
  var out = Buffer.alloc(32)
  return blake2b_(32).update(buffer).digest(out)
}

function blake(buffer) {
  return blake_('blake256').update(buffer).digest()
}

var payload = Buffer.alloc(32)
var hashed = blake2b(payload)

var hashed2 = blake(payload)

console.log(payload)
console.log(hashed)
console.log(hashed2)
