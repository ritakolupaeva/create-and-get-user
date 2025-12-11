from helpers.user_api import UserAPI


def test_create_and_get_user(generated_user_data):
    generated_id, generated_username, user_payload = generated_user_data
    sent_email = user_payload[0]["email"]

    # 1. Create user
    create_resp = UserAPI.create_user(user_payload)
    assert create_resp.status_code == 200
    body = create_resp.json()
    assert body["code"] == 200
    assert body["message"] == "ok"
    print(f"\nUser created with ID: {generated_id}, Username: '{generated_username}', Email: '{sent_email}'")

    # 2. Get user
    get_resp = UserAPI.get_user(generated_username)
    assert get_resp.status_code == 200
    user_data = get_resp.json()
    print(f"User received with ID: {user_data['id']}, Username: '{user_data['username'],}', Email: '{user_data['email'],}'")

    # 3. Assertions
    assert user_data["id"] == generated_id
    assert user_data["username"] == generated_username
    assert user_data["email"] == sent_email

    # 2. If you need - Delete user
    get_resp = UserAPI.delete_user(generated_username)
    assert get_resp.status_code == 200
    user_data = get_resp.json()
    print(f"User with ID: {generated_id} deleted.")