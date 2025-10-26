from abc import ABC
from service.ethereum_transactions import EthereumTransactions

class TransactionFetcherFactory(ABC):
    @staticmethod
    def fetch_transactions(source, address, api_key=None, base_url=None):
        if source == 'ether':
            EthereumTransactions(api_key=api_key, base_url=base_url).get_ethereum_transactions(address=address)
        else:
            raise ValueError('Invalid source')
