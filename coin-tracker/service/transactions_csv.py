from service.ethereum_transactions import EthereumTransactions
from factory.transaction_fetcher_factory import TransactionFetcherFactory

class TransactionsCsv:
    def generate_csv(self, source):
        transactions = TransactionFetcherFactory(source)