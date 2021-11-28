from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class GoogleHomePage:

    def __init__(self, driver):
        self.driver = driver

    def _click_the_gmail_link(self):
        self._click_the_link("Gmail")

    def _click_the_images_link(self):
        self._click_the_link("Images")

    def _search_filter_phrase(self, search_phrase):
        self.driver.find_element_by_xpath("//*[@title='Search']").send_keys(search_phrase)

    def _click_the_google_search_button(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

    def _search_filer_phrase_and_click_enter_key(self):
        self.driver.find_element_by_xpath("//*[@title='Search']").send_keys(Keys.ENTER)

    def _click_the_link(self, text):
        links = self.driver.find_elements_by_class_name("gb_f")
        for link in links:
            if link.text == text:
                link.click()
                break

    def _click_the_accept_button_in_confirm_form(self):
        buttons = self.driver.find_elements_by_class_name("QS5gu")
        self._wait_for_element("QS5gu")
        for button in buttons:
            if button.text == "I agree":
                button.click()
                break

    def _log_in_button_is_displayed(self):
        self.driver.find_element_by_xpath("//*[text()='Sign in']").is_displayed()

    def _wait_for_element(self, class_name, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
