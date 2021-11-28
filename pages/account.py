
class AccountPage:
    ABOUT_NAME = "about"

    def __init__(self, driver):
        self.driver = driver

    def _sign_in_button_is_displayed(self):
        self.driver.find_element_by_xpath("//*[@data-action='sign in']").is_displayed()

    def _get_the_account_page_url(self):
        return self.driver.current_url
