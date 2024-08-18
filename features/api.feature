Feature: CRUD API

  Scenario: Create an item
    Given the API is running
    When I send a POST request to "/items" with data "{"name": "Item 1"}"
    Then the response status code should be 201
    And the response should contain "{"name": "Item 1"}"

  Scenario: Get all items
    Given the API is running
    When I send a GET request to "/items"
    Then the response status code should be 200
    And the response should contain "[]"
