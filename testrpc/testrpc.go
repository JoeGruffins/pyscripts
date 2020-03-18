package main

import (
	"encoding/hex"
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"

	flags "github.com/jessevdk/go-flags"

	"github.com/decred/dcrd/chaincfg/chainhash"
	"github.com/decred/dcrd/dcrutil/v2"
	"github.com/decred/dcrd/rpcclient/v4"
)

type config struct {
	Username string `long:"username"`
	Password string `long:"password"`
}

// fileExists reports whether the named file or directory exists.
func fileExists(name string) bool {
	if _, err := os.Stat(name); err != nil {
		if os.IsNotExist(err) {
			return false
		}
	}
	return true
}

var ticketHash = "7edfa02ab7b532b2c3f7c8260052cc359e22783aeed460ca314584600cb1d05d"

func connectWalletRPC() (*rpcclient.Client, error) {
	home := dcrutil.AppDataDir("dcrwallet", false)
	conf := filepath.Join(home, "dcrwallet.conf")
	if !fileExists(conf) {
		return nil, errors.New("no config file")
	}
	cert := filepath.Join(home, "rpc.cert")
	dcrwCert, err := ioutil.ReadFile(cert)
	if err != nil {
		return nil, err
	}
	cfg := new(config)
	parser := flags.NewParser(cfg, flags.Default)
	// ignoring errors for extra flags
	_ = flags.NewIniParser(parser).ParseFile(conf)
	host := "127.0.0.1:19110"

	connCfgWallet := &rpcclient.ConnConfig{
		Host:         host,
		Endpoint:     "ws",
		User:         cfg.Username,
		Pass:         cfg.Password,
		Certificates: dcrwCert,
	}
	dcrwClient, err := rpcclient.New(connCfgWallet, nil)
	if err != nil {
		return nil, err
	}
	// Ensure the wallet is reachable.
	_, err = dcrwClient.Version()
	if err != nil {
		return nil, fmt.Errorf("unable to get wallet RPC version: %v", err)
	}
	return dcrwClient, nil
}

func main() {
	w, err := connectWalletRPC()
	if err != nil {
		panic(err)
	}
	th, err := hex.DecodeString(ticketHash)
	if err != nil {
		panic(err)
	}
	for i, j := 0, len(th)-1; i < j; i, j = i+1, j-1 {
		th[i], th[j] = th[j], th[i]
	}
	hash, err := chainhash.NewHash(th)
	if err != nil {
		panic(err)
	}
	res1, err := w.GetTransaction(hash)
	if err != nil {
		panic(err)
	}
	fmt.Println(res1)
	res2, err := w.GetRawTransaction(hash)
	if err != nil {
		panic(err)
	}
	fmt.Println(res2)
	err = w.AddTicket(res2)
	if err != nil {
		panic(err)
	}
}
