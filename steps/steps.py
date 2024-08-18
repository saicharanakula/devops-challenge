import requests
from behave import given, when, then

@given('the API is running')
def step_impl(context):
    # Use the base_url passed as a CLI argument or the default one
    pass  # base_url is already set in context from environment.py

@given('I have added an item with data \'{data}\'')
def step_impl(context, data):
    url = f"{context.base_url}/items"
    response = requests.post(url, json=eval(data))
    context.response = response
    assert response.status_code == 201

@when('I send a POST request to "{endpoint}" with data \'{data}\'')
def step_impl(context, endpoint, data):
    url = f"{context.base_url}{endpoint}"
    response = requests.post(url, json=eval(data))
    context.response = response

@when('I send a PUT request to "{endpoint}" with data \'{data}\'')
def step_impl(context, endpoint, data):
    url = f"{context.base_url}{endpoint}"
    response = requests.put(url, json=eval(data))
    context.response = response

@when('I send a DELETE request to "{endpoint}"')
def step_impl(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    response = requests.delete(url)
    context.response = response

@when('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    response = requests.get(url)
    context.response = response

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response should contain \'{expected}\'')
def step_impl(context, expected):
    assert context.response.json() == eval(expected)
