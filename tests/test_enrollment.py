import pytest
import httpx
from base64 import b64encode

BASE_URL = "http://localhost:8000"

def basic_auth_header(username="admin", password="1234"):
    credentials = f"{username}:{password}"
    encoded = b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

@pytest.mark.asyncio
async def test_enrollment_valid_and_duplicate():
    age_group = {
        "name": "60-65",
        "min_age": 60,
        "max_age": 65
    }

    async with httpx.AsyncClient() as client:
        await client.post(
            f"{BASE_URL}/age-groups/",
            json=age_group,
            headers=basic_auth_header()
        )

        enrollment = {
            "name": "João da Silva",
            "age": 61,
            "cpf": "12345678999"
        }

        response = await client.post(
            f"{BASE_URL}/enrollments/",
            json=enrollment,
            headers=basic_auth_header()
        )
        print("STATUS:", response.status_code)
        print("BODY:", response.text)

        assert response.status_code == 200
        assert "id" in response.json()

        response = await client.get(
            f"{BASE_URL}/enrollments/status/12345678999",
            headers=basic_auth_header()
        )
        assert response.status_code == 200
        assert response.json()["name"] == "João da Silva"

        response = await client.post(
            f"{BASE_URL}/enrollments/",
            json=enrollment,
            headers=basic_auth_header()
        )
        assert response.status_code == 400
        assert "já existe" in response.text.lower()
