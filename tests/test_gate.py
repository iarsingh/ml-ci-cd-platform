from fastapi.testclient import TestClient
from mlcicd.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'lint': True, 'tests': True, 'helm': True, 'terraform': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'lint': True, 'tests': True, 'helm': True}).json()
    assert bad["passed"] is False
    assert "terraform" in bad["failed"]
