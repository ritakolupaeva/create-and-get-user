import random
import pytest
from datetime import datetime
from faker import Faker
fake = Faker()


@pytest.fixture
def generated_user_data():
    """Generate unique ID and username"""
    now = datetime.now()
    generated_id = int(now.strftime("%H%M%d%m"))
    generated_username = f"{fake.first_name()}_{fake.last_name()}{generated_id}"
    generated_email = generated_username + '@test.com'

    user_payload = [
        {
            "id": generated_id,
            "username": generated_username,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": generated_email,
            "password": fake.password(length=10),
            "phone": fake.msisdn(),
            "userStatus": random.choice([0, 1])
        }
    ]
    
    return generated_id, generated_username, user_payload
