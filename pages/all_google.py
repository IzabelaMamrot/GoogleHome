from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AllGooglePage:

    def __init__(self, driver):
        self.driver = driver

    def _wait_and_get_the_list_of_results(self):
        list_of_result = []
        self._wait_for_element("LC20lb")
        rows = self.driver.find_elements_by_class_name("LC20lb")
        for row in rows:
            list_of_result.append(row.text)
        return list_of_result

    def _wait_for_element(self, class_name, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
