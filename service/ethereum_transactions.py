import os
from datetime import datetime
from api_client.ethereum_api_client import EthereumApiClient
from utils.csv_parser import CsvParser
from formatter.ethereum_transaction_formatter import EthereumTransactionFormatter

class EthereumTransactions:
    def __init__(self, large_txn_count, api_key=None, base_url=None):
        self.api_client = EthereumApiClient(api_key=api_key, base_url=base_url)
        self.active_block_range = self._active_block_range()
        self.large_txn_count = large_txn_count

    def get_filename(self, address):
        output_dir="exports"
        os.makedirs(output_dir, exist_ok=True)
        address_short = f"{address[:5]}"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/{address_short}_{timestamp}.csv"
        return filename

    def get_ethereum_transactions(self, address):
        file_name = self.get_filename(address)
        include_types = ['normal', 'internal', 'token', 'nft']

        if 'normal' in include_types:
            print(f"Streaming normal transactions to...")
            CsvParser().stream_to_csv(self.fetch_normal_transactions(self.large_txn_count, address), file_name)
            print(f"Completed normal transactions to...")

        if 'internal' in include_types:
            print(f"Streaming internal transactions to...")
            CsvParser().stream_to_csv(self.fetch_internal_transactions(self.large_txn_count, address), file_name)
            print(f"Completed internal transactions to...")

        if 'token' in include_types:
            print(f"Streaming token transactions to...")
            CsvParser().stream_to_csv(self.fetch_token_transactions(self.large_txn_count, address), file_name)
            print(f"Completed token transactions to...")

        if 'nft' in include_types:
            print(f"Streaming NFT transactions to...")
            CsvParser().stream_to_csv(self.fetch_nft_transactions(self.large_txn_count, address), file_name)
            print(f"Completed NFT transactions to...")

    def fetch_normal_transactions(self, large_txn_count, address):
        total_fetched = 0
        if large_txn_count:
            for current_range in self.active_block_range:
                current_start, current_end = current_range["start"], current_range["end"]
                print(f"Processing block from {current_start} to {current_end}")

                page = 1
                while True:
                    params = {
                        "chainid": "1",
                        "module": "account",
                        "action": "txlist",
                        "address": address,
                        "startblock": current_start,
                        "endblock": current_end,
                        "page": page,
                        "offset": self.api_client.max_offset,
                        "sort": "asc"
                    }

                    transactions = self.api_client.make_request(params)

                    if not transactions:
                        break
                    if transactions:
                        print(f"found transaction in block from {current_start} to {current_end}")

                    total_fetched += len(transactions)
                    print(f"Blocks {current_start:,}-{current_end:,}, Page {page}: {len(transactions)} txs (Total: {total_fetched:,})")

                    for tx in transactions:
                        yield EthereumTransactionFormatter().format_transaction(tx)

                    # If we got less than max_offset, no more pages for this block range
                    if len(transactions) < self.api_client.max_offset:
                        break

                    page += 1

                    # Safety check: if page * offset > 10000, move to next block range
                    if page * self.api_client.max_offset > 10000:
                        print(f"Reached pagination limit, moving to next block range")
                        break
        else:
            params = {
                "chainid": "1",
                "module": "account",
                "action": "txlist",
                "address": address,
                "sort": "asc"
            }
            transactions = self.api_client.make_request(params)
            if transactions:
                for tx in transactions:
                    yield EthereumTransactionFormatter().format_transaction(tx)

        print(f"Completed: {total_fetched:,} normal transactions fetched\n")

    def fetch_internal_transactions(self, large_txn_count, address):
        total_fetched = 0

        if large_txn_count:
            for current_range in self.active_block_range:
                current_start, current_end = current_range["start"], current_range["end"]
                print(f"Processing block from {current_start} to {current_end}")

                page = 1
                while True:
                    params = {
                        "chainid": "1",
                        "module": "account",
                        "action": "txlistinternal",
                        "address": address,
                        "startblock": current_start,
                        "endblock": current_end,
                        "page": page,
                        "offset": self.api_client.max_offset,
                        "sort": "asc"
                    }

                    transactions = self.api_client.make_request(params)

                    if not transactions:
                        break

                    if transactions:
                        print(f"found transaction in block from {current_start} to {current_end}")

                    total_fetched += len(transactions)
                    print(f"Blocks {current_start:,}-{current_end:,}, Page {page}: {len(transactions)} txs (Total: {total_fetched:,})")

                    for tx in transactions:
                        yield EthereumTransactionFormatter().format_transaction(tx)

                    if len(transactions) < self.api_client.max_offset:
                        break

                    page += 1

                    if page * self.api_client.max_offset > 10000:
                        print(f"Reached pagination limit, moving to next block range")
                        break
        else:
            params = {
                "chainid": "1",
                "module": "account",
                "action": "txlist",
                "address": address,
                "sort": "asc"
            }
            transactions = self.api_client.make_request(params)
            if transactions:
                for tx in transactions:
                    yield EthereumTransactionFormatter().format_transaction(tx)

        print(f"Completed: {total_fetched:,} internal transactions fetched\n")

    def fetch_token_transactions(self, large_txn_count, address):
        total_fetched = 0

        if large_txn_count:
            for current_range in self.active_block_range:
                current_start, current_end = current_range["start"], current_range["end"]
                print(f"Processing block from {current_start} to {current_end}")

                page = 1
                while True:
                    params = {
                        "chainid": "1",
                        "module": "account",
                        "action": "tokentx",
                        "address": address,
                        "startblock": current_start,
                        "endblock": current_end,
                        "page": page,
                        "offset": self.api_client.max_offset,
                        "sort": "asc"
                    }

                    transactions = self.api_client.make_request(params)

                    if not transactions:
                        break
                    if transactions:
                        print(f"found transaction in block from {current_start} to {current_end}")

                    total_fetched += len(transactions)
                    print(f"Blocks {current_start:,}-{current_end:,}, Page {page}: {len(transactions)} txs (Total: {total_fetched:,})")

                    for tx in transactions:
                        yield EthereumTransactionFormatter().format_transaction(tx)

                    if len(transactions) < self.api_client.max_offset:
                        break

                    page += 1

                    if page * self.api_client.max_offset > 10000:
                        print(f"Reached pagination limit, moving to next block range")
                        break
        else:
            params = {
                "chainid": "1",
                "module": "account",
                "action": "txlist",
                "address": address,
                "sort": "asc"
            }
            transactions = self.api_client.make_request(params)
            if transactions:
                for tx in transactions:
                    yield EthereumTransactionFormatter().format_transaction(tx)

        print(f"Completed: {total_fetched:,} token transactions fetched\n")

    def fetch_nft_transactions(self, large_txn_count, address):
        total_fetched = 0

        if large_txn_count:
            for current_range in self.active_block_range:
                current_start, current_end = current_range["start"], current_range["end"]
                print(f"Processing block from {current_start} to {current_end}")

                page = 1
                while True:
                    params = {
                        "chainid": "1",
                        "module": "account",
                        "action": "tokennfttx",
                        "address": address,
                        "startblock": current_start,
                        "endblock": current_end,
                        "page": page,
                        "offset": self.api_client.max_offset,
                        "sort": "asc"
                    }

                    transactions = self.api_client.make_request(params)

                    if not transactions:
                        break
                    if transactions:
                        print(f"found transaction in block from {current_start} to {current_end}")

                    total_fetched += len(transactions)
                    print(f"Blocks {current_start:,}-{current_end:,}, Page {page}: {len(transactions)} txs (Total: {total_fetched:,})")

                    for tx in transactions:
                        yield EthereumTransactionFormatter().format_transaction(tx)

                    if len(transactions) < self.api_client.max_offset:
                        break

                    page += 1

                    if page * self.api_client.max_offset > 10000:
                        print(f"Reached pagination limit, moving to next block range")
                        break
        else:
            params = {
                "chainid": "1",
                "module": "account",
                "action": "txlist",
                "address": address,
                "sort": "asc"
            }
            transactions = self.api_client.make_request(params)
            if transactions:
                for tx in transactions:
                    yield EthereumTransactionFormatter().format_transaction(tx)

        print(f"Completed: {total_fetched:,} NFT transactions fetched\n")

    def _active_block_range(self):
        active_block_range = []
        end_block = self._get_latest_block()
        current_start = 0
        while current_start < end_block:
            current_end = min(current_start + self.api_client.block_range, end_block)
            active_block_range.append({ "start": current_start, "end": current_end })
            current_start = current_end + 1
        return active_block_range

    def _get_latest_block(self):
        """Get the latest block number"""
        params = {
            "chainid": "1",
            "module": "proxy",
            "action": "eth_blockNumber"
        }
        result = self.api_client.make_request(params)
        if result:
            try:
                return int(result, 16) if isinstance(result, str) else result
            except:
                return 99999999
        return 99999999
