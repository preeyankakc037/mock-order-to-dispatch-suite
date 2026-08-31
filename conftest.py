import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_headers():
    api_key = os.getenv("REQRES_API_KEY")
    return {
        "Content-Type": "application/json",
        "x-api-key": api_key,
    }