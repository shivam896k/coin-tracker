from abc import ABC
from service.ethereum_transactions import EthereumTransactions

class TransactionFetcherFactory(ABC):
    @staticmethod
    def fetch_transactions(source, large_txn_count, address, api_key=None, base_url=None):
        if source == 'ether':
            EthereumTransactions(large_txn_count, api_key=api_key, base_url=base_url).get_ethereum_transactions(address=address)
        else:
            raise ValueError('Invalid source')
