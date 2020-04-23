#!/usr/bin/env python3
import matplotlib.pyplot as plt
from urllib.parse import urlunsplit
from decred.dcr import rpc
import os

from decred.util import helpers


def cfg():
    dcrdCfgDir = helpers.appDataDir("dcrd")
    cfgPath = os.path.join(dcrdCfgDir, "dcrd.conf")
    if not os.path.isfile(cfgPath):
        return None
    cfg = helpers.readINI(cfgPath, ["rpcuser", "rpcpass", "rpccert"])
    assert "rpcuser" in cfg
    assert "rpcpass" in cfg
    if "rpccert" not in cfg:
        cfg["rpccert"] = os.path.join(dcrdCfgDir, "rpc.cert")
    if "rpclisten" not in cfg:
        cfg["rpclisten"] = "localhost:9109"
    return cfg


dcrdConfig = cfg()
node = rpc.Client(
    urlunsplit(("https", dcrdConfig["rpclisten"], "/", "", "")),
    dcrdConfig["rpcuser"],
    dcrdConfig["rpcpass"],
    dcrdConfig["rpccert"],
)
block = node.getBlock(node.getBestBlockHash(), verboseTx=True)
fees = []

under1 = 0
over1 = 0
over300 = 0
about10 = 0
about10sum = 0
while len(fees) < 10000:
    for tx in block.rawTx[1:]:
        fee = sum(vin.amountIn for vin in tx.vin) - sum(vout.value for vout in tx.vout)
        atoms = fee * 1e8
        sizeInKB = tx.tx.serializeSize() / 1000
        atomsPerKB = atoms/sizeInKB
        ratePerDefault = atomsPerKB / 1e4
        fees.append(ratePerDefault)
        r = ratePerDefault
        if r > 300:
            over300 += 1
        if r < 1:
            under1 += 1
            print("under1", r)
        if r > 1.1:
            over1 += 1
        if r > 9.9 and r < 15.1:
            print("between 10 15", r)
            about10 += 1
            about10sum += r
    block = node.getBlock(block.previousHash, verboseTx=True)

n = len(fees)
print("all", n)
print("under1", under1)
print("over1", over1)
print("about10", about10, about10/over1, about10sum/about10)
print("over300", over300)

plt.hist(fees, bins=100, rwidth=0.8, color="#333333")
plt.show()
