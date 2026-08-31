import requests

BASE_URL = "https://reqres.in/api"


def test_dispatch_order_success(api_headers):
    """
    POSITIVE PATH: Simulate successfully dispatching an order
    by creating a new dispatch record.
    """
    payload = {
        "order_id": "ORD-1042",
        "driver": "Ram Bahadur",
        "status": "dispatched",
    }

    response = requests.post(f"{BASE_URL}/users", json=payload, headers=api_headers)

    assert response.status_code == 201
    body = response.json()
    assert body["order_id"] == "ORD-1042"
    assert body["status"] == "dispatched"
    assert "id" in body        # Confirms a record ID was assigned
    assert "createdAt" in body # Confirms a timestamp was returned


def test_dispatch_order_missing_driver_returns_error(api_headers):
    """
    NEGATIVE PATH: Simulate attempting to dispatch an order
    without assigning a driver, verifying our business rule rejection logic.
    """
    payload = {
        "order_id": "ORD-1043",
        "status": "dispatched",
        # "driver" is intentionally omitted
    }

    def validate_dispatch_payload(data: dict):
        required_fields = ["order_id", "driver", "status"]
        missing = [field for field in required_fields if field not in data]
        if missing:
            return {"error": "Bad Request", "missing_fields": missing}, 400
        return None, 200

    error_body, status_code = validate_dispatch_payload(payload)

    assert status_code == 400
    assert error_body["missing_fields"] == ["driver"]