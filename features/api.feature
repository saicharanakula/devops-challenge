Feature: CRUD API

  Scenario: Create an item
    Given the API is running
    When I send a POST request to "/items" with data '{"name": "Item 1"}'
    Then the response status code should be 201
    And the response should contain '{"name": "Item 1"}'

  Scenario: Get all items
    Given the API is running
    When I send a GET request to "/items"
    Then the response status code should be 200
    And the response should contain '[{"name": "Item 1"}]'

  Scenario: Update an item
    Given the API is running
    When I send a PUT request to "/items/0" with data '{"name": "Updated Item"}'
    Then the response status code should be 200
    And the response should contain '{"name": "Updated Item"}'

  Scenario: Delete an item
    Given the API is running
    When I send a DELETE request to "/items/0"
    Then the response status code should be 204
