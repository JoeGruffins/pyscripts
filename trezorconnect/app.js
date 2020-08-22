var tc = require('trezor-connect').default;
var DEVICE_EVENT = require('trezor-connect').DEVICE_EVENT;
var DEVICE = require('trezor-connect').DEVICE;
const hardeningConstant = 0x80000000;
const coin = "decred"

async function main() {
  function init() {
  return tc.init({
      connectSrc: 'https://localhost:8088/',
      lazyLoad: true,
      popup: false,
      manifest: {
          email: 'joegruffins@gmail.com',
          appUrl: 'https://github.com/decred/decrediton',
      },
      webusb: true
    })
  }
  function getAddr() {
    const path = [
      (44 | hardeningConstant) >>> 0, // purpose
      (42 | hardeningConstant) >>> 0, // coin type
      (0 | hardeningConstant) >>> 0, // account
      0, // branch
      0  // index
    ]
    console.log(path)
    return tc.getAddress({
	    path: path,
      coin: coin,
      showOnTrezor: false
    })
  }
  function getAcct() {
    var path = [
      (44 | hardeningConstant) >>> 0, // purpose
      (42 | hardeningConstant) >>> 0, // coin type
      (0 | hardeningConstant) >>> 0, // account
    ]
    return tc.getPublicKey({
      path: path,
      coin: coin,
      showOnTrezor: false
    })
  }
  try {
    await init()
    let res = await getAddr()
    console.log("Address: %s", res.payload.address)
    res = await getAcct()
    console.log(res.payload)
  } catch(e) {
    console.log(e);
  }
}

main()
//tc.on(DEVICE_EVENT, (event) => {
//	console.log(event)
//});
