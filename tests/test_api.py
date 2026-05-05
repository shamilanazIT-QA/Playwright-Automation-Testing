from playwright.sync_api import sync_playwright, expect


def test_get_user_details():
    with sync_playwright() as p:
        # We use request.new_context instead of browser.new_context
        api_request_context = p.request.new_context(base_url="https://reqres.in")

        # 1. Send a GET request to fetch user data
        response = api_request_context.get("/api/users/2")

        # 2. Assert the status code is 200 (OK)
        assert response.ok
        assert response.status == 200

        # 3. Check the actual data inside the response
        user_data = response.json()
        print(f"User Email: {user_data['data']['email']}")

        # Professional Assertion: Verify the user's name is Janet
        assert user_data['data']['first_name'] == "Janet"

        api_request_context.dispose()