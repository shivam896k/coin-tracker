from datetime import datetime

class EthereumTransactionFormatter:
    def format_transaction(self, transaction):
        gas_used = int(transaction.get("gasUsed", 0))
        gas_price = int(transaction.get("gasPrice", 0))
        tx_fee = (gas_used * gas_price)

        return {
            "transaction_hash": transaction.get("hash", ""),
            "timestamp": datetime.fromtimestamp(int(transaction.get("timeStamp", 0))).strftime("%Y-%m-%d %H:%M:%S"),
            "from_address": transaction.get("from", ""),
            "to_address": transaction.get("to", ""),
            "transaction_type": "ETH",
            "contract_address": transaction.get("contractAddress", ""),
            "asset": "ETH",
            "value": transaction.get("value", 0),
            "gas_fee": f"{tx_fee:.18f}"
        }
