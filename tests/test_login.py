from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage

scenarios('Login.feature')

@given("the user is on the Saucedemo login page")
def navigate_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when('the user enters "<username>" and "<password>"')
def enter_credentials(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)

@when("the user clicks on the login button")
def click_login_button():
    # The login button click is already handled in the login method of the page object
    pass

@then("the user should be redirected to the inventory page")
def verify_inventory_page(page):
    assert "inventory.html" in page.url

@then('the user should see an error message "Sorry, this user has been locked out."')
def verify_locked_out_error(page):
    login_page = LoginPage(page)
    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_message

@then('the user should see an error message "Username and password do not match any user in this service."')
def verify_invalid_credentials_error(page):
    login_page = LoginPage(page)
    error_message = login_page.get_error_message()
    assert "Username and password do not match any user in this service." in error_message
