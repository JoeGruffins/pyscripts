from tinydecred.pydecred import txscript
from tinydecred.pydecred import nets
from tinydecred.pydecred import calc

# ticket fee
ticketfee = 6648767171
# relay fee
relayfee = 5420
# block height
bh = 221919
# pool fee
poolfee = 0.5
# network params
params = nets.testnet

fee = txscript.stakePoolTicketFee(ticketfee, relayfee, bh, poolfee,
                                  calc.SubsidyCache(params), params)
print(fee)
