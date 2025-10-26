import traceback
import argparse
import os
from factory.transaction_fetcher_factory import TransactionFetcherFactory
from utils.env_helper import load_env

class GenerateReport:
    """A simple task report_generator CLI application"""

    def __init__(self):
        self.tasks = []
        self.parser = self.create_parser()

    def create_parser(self):
        parser = argparse.ArgumentParser(
            description='Task Executor'
        )
        parser.add_argument(
            '-a', '--address',
            required=True,
            help='Input ethereum address'
        )
        parser.add_argument(
            '-s', '--size',
            required=True,
            help='Input ethereum txn count'
        )
        return parser

    def execute_report(self, eth_address, large_txn_count=False):
        print(f"Generating report...")
        api_key = os.environ.get('ETHER_SCAN_API_KEY')
        base_url = os.environ.get('ETHER_SCAN_BASE_URL')
        large_txn = large_txn_count == 'true'
        TransactionFetcherFactory.fetch_transactions('ether', large_txn, eth_address, api_key=api_key, base_url=base_url)

    def run(self, args=None):
        try:
            parsed_args = self.parser.parse_args(args)
            self.execute_report(parsed_args.address, parsed_args.size)
        except Exception as e:
            traceback.print_exc()

def main():
    load_env()
    report_generator = GenerateReport()
    report_generator.run()

if __name__ == '__main__':
    main()
