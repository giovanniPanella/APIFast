import pytest
import httpx
from base64 import b64encode

BASE_URL = "http://localhost:8000"

def basic_auth_header(username="admin", password="1234"):
    credentials = f"{username}:{password}"
    encoded = b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

@pytest.mark.asyncio
async def test_create_and_list_age_groups():
    # Cria um grupo etário
    group = {"name": "50-55", "min_age": 50, "max_age": 55}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/age-groups",
            json=group,
            headers=basic_auth_header()
        )
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["name"] == "50-55"

        # Lista grupos
        response = await client.get(
            f"{BASE_URL}/age-groups",
            headers=basic_auth_header()
        )
        assert response.status_code == 200
        groups = response.json()
        assert any(g["name"] == "50-55" for g in groups)

