from service.ethereum_transactions import EthereumTransactions


class FakeApiClient:
    def __init__(self):
        self.max_offset = 1000
        self.block_range = 30

    def make_request(self, params):
        if params.get("action") == "eth_blockNumber":
            return "0x41"  # 65
        return []

def test_get_latest_block_and_active_range(monkeypatch):
    et = EthereumTransactions(api_key=None, base_url=None)
    et.api_client = FakeApiClient()

    latest = et._get_latest_block()
    assert isinstance(latest, int) and latest == 65

    ranges = et._active_block_range()
    assert ranges[0]["start"] == 0
    assert ranges[-1]["end"] == 65

def test_get_filename_contains_exports_and_short_address():
    et = EthereumTransactions(api_key=None, base_url=None)
    filename = et.get_filename("0xfabcdef")
    assert "exports" in filename
    assert filename.startswith("exports/") or "/exports/" in filename
    assert filename.count("_") >= 1
