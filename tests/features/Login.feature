Feature: Login functionality on Saucedemo website

  Scenario Outline: Successful login with valid credentials
    Given the user is on the Saucedemo login page
    When the user enters "<username>" and "<password>"
    And the user clicks on the login button
    Then the user should be redirected to the inventory page

    Examples:
      | username               | password      |
      | standard_user          | secret_sauce  |
      | problem_user           | secret_sauce  |
      | performance_glitch_user| secret_sauce  |

  Scenario Outline: Unsuccessful login with locked out user
    Given the user is on the Saucedemo login page
    When the user enters "<username>" and "<password>"
    And the user clicks on the login button
    Then the user should see an error message "Sorry, this user has been locked out."

    Examples:
      | username       | password      |
      | locked_out_user| secret_sauce  |

  Scenario Outline: Unsuccessful login with valid user and invalid password
    Given the user is on the Saucedemo login page
    When the user enters "<username>" and "<password>"
    And the user clicks on the login button
    Then the user should see an error message "Username and password do not match any user in this service."

    Examples:
      | username       | password        |
      | locked_out_user| invalid_password|

  Scenario Outline: Unsuccessful login with non-existent user
    Given the user is on the Saucedemo login page
    When the user enters "<username>" and "<password>"
    And the user clicks on the login button
    Then the user should see an error message "Username and password do not match any user in this service."

    Examples:
      | username  | password      |
      | error_user| secret_sauce  |
      | visual_user| secret_sauce |
