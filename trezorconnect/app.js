var tc = require('trezor-connect').default;
var DEVICE_EVENT = require('trezor-connect').DEVICE_EVENT;
var DEVICE = require('trezor-connect').DEVICE;

tc.init({
    connectSrc: 'https://localhost:8088/',
    lazyLoad: true,
    manifest: {
        email: 'joegruffins@gmail.com',
        appUrl: 'https://github.com/decred/decrediton',
    },
    webusb: true
})
.then(() => {
    tc.getAddress({
	path: "m/49'/0'/0'/0/2",
    	coin: "btc"
    })
        .then(addr => {
            console.log("Address: %s", addr.payload)
        })
        .catch(err => console.log(err));
})
.catch(error => {
    console.log('TrezorConnect init error', error)
});

tc.on(DEVICE_EVENT, (event) => {
	console.log(event)
});
