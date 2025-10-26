from formatter.ethereum_transaction_formatter import EthereumTransactionFormatter


def test_format_transaction_basic():
    tx = {
        "gasUsed": "21000",
        "gasPrice": "1000000000",
        "timeStamp": "1600000000",
        "hash": "0xabc",
        "from": "0xfrom",
        "to": "0xto",
        "contractAddress": "0x0",
        "value": "123"
    }

    formatted = EthereumTransactionFormatter().format_transaction(tx)

    assert formatted["transaction_hash"] == "0xabc"
    assert formatted["from_address"] == "0xfrom"
    assert formatted["to_address"] == "0xto"
    assert float(formatted["gas_fee"]) == 21000 * 1_000_000_000
    assert formatted["transaction_type"] == "ETH"
    assert formatted["asset"] == "ETH"
