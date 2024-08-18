import requests
from behave import given, when, then

@given('the API is running')
def step_impl(context):
    context.base_url = "http://localhost"

@when('I send a {method} request to "{endpoint}" with data "{data}"')
def step_impl(context, method, endpoint, data):
    url = f"{context.base_url}{endpoint}"
    response = requests.request(method.upper(), url, json=eval(data))
    context.response = response

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response should contain "{expected}"')
def step_impl(context, expected):
    assert context.response.json() == eval(expected)
