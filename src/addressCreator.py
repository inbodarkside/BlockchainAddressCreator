from mnemonic import Mnemonic
from web3 import Web3


def createNewAddress(mnemolanguage,provider,password):
    mnemo = Mnemonic(mnemolanguage)
    words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(words, passphrase=str(password))
    w3 = Web3(Web3.HTTPProvider(provider))
    account = w3.eth.account.privateKeyToAccount(seed[:32])
    private_key = account.privateKey
    public_key = account.address
    return private_key.hex(), words, public_key
