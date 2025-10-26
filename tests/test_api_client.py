from api_client.ethereum_api_client import EthereumApiClient
from unittest.mock import Mock


def test_make_request_success(monkeypatch):
    mock_get = Mock()
    mock_resp = Mock()
    mock_resp.json.return_value = {"status": "1", "result": [{"hash": 'sdjfl'}]}
    mock_get.return_value = mock_resp

    monkeypatch.setattr("api_client.ethereum_api_client.requests.get", mock_get)

    client = EthereumApiClient(api_key="k", base_url="http://example.com")
    res = client.make_request({"foo": "bar"})
    assert isinstance(res, list)
    assert res[0]["hash"] == 'sdjfl'


def test_make_request_no_transactions(monkeypatch):
    mock_get = Mock()
    mock_resp = Mock()
    mock_resp.json.return_value = {"message": "No transactions found"}
    mock_get.return_value = mock_resp

    monkeypatch.setattr("api_client.ethereum_api_client.requests.get", mock_get)

    client = EthereumApiClient(api_key="k", base_url="http://example.com")
    res = client.make_request({"foo": "bar"})
    assert res == []
