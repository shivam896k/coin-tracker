import requests
import time
import os

class EthereumApiClient:
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or os.environ.get('ETHEREUM_API_KEY')
        self.base_url = base_url or os.environ.get('ETHEREUM_BASE_URL')
        self.max_offset = 10_000
        self.block_range = 100_000

    def make_request(self, params):
        try:
            params['apikey'] = self.api_key
            response = requests.get(self.base_url, params=params, timeout=30)
            data = response.json()

            if data.get("status") == "1":
                return data.get("result", [])
            elif data.get("message") == "No transactions found":
                return []
            elif data.get("id") == 83:
                return data.get("result")
            else:
                error_msg = data.get('result', data.get('message', 'Unknown error'))
                if "rate limit" in str(error_msg).lower():
                    print(f"Rate limit hit, waiting 2 seconds...")
                    time.sleep(2)
                    return self._make_request(params)
                print(f"API Error: {error_msg}")
                return []
        except requests.exceptions.Timeout:
            print("Request timeout, retrying...")
            time.sleep(2)
            return self._make_request(params)
        except Exception as e:
            print(f"Request failed: {e}")
            return []
