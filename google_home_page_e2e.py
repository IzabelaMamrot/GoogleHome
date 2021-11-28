import unittest

from selenium import webdriver

from pages import GoogleHomePage, AccountPage, GoogleImagePage, AllGooglePage


class TestGooglePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.google.com/")
        cls.google_home_page = GoogleHomePage(cls.driver)
        cls.google_home_page._click_the_accept_button_in_confirm_form()
        cls.account_page = AccountPage(cls.driver)
        cls.google_image_page = GoogleImagePage(cls.driver)
        cls.all_google_page = AllGooglePage(cls.driver)

    def test_google_link_redirect_to_account_page_if_user_is_not_log_in(self):
        self.google_home_page._log_in_button_is_displayed()
        self.google_home_page._click_the_gmail_link()
        self.assertIn(self.account_page.ABOUT_NAME, self.account_page._get_the_account_page_url(),
                      "The url for account page is incorrect. In link is not word {}"
                      .format(self.account_page.ABOUT_NAME))
        self.account_page._sign_in_button_is_displayed()

    def test_image_link_redirect_to_google_image(self):
        self.google_home_page._click_the_images_link()
        self.google_home_page._click_the_accept_button_in_confirm_form()
        self.assertIn(self.google_image_page.IMG_NAME, self.google_image_page._get_the_image_page_url(),
                      "The url for image page is incorrect. In link is not word {}"
                      .format(self.google_image_page.IMG_NAME))
        self.assertEqual(self.google_image_page._find_the_image_text_in_google_icon(),
                         self.google_image_page.IMAGES_NAME, "In Google images icon is not visible the {} word"
                         .format(self.google_image_page.IMAGES_NAME))

    def test_enter_search_filter_with_google_search_button(self):
        search_phrase = "Duco"
        self.google_home_page._search_filter_phrase(search_phrase)
        self.google_home_page._click_the_google_search_button()
        first_result = self.all_google_page._wait_and_get_the_list_of_results()[0]
        self.assertNotEqual(len(self.all_google_page._wait_and_get_the_list_of_results()), 0,
                            "The search result is empty")
        self.assertIn(search_phrase, first_result,
                      "In search result for {} there are not results".format(search_phrase))

    def test_enter_search_filter_with_enter_key(self):
        search_phrase = "Duco"
        self.google_home_page._search_filter_phrase(search_phrase)
        self.google_home_page._search_filer_phrase_and_click_enter_key()
        self.assertNotEqual(len(self.all_google_page._wait_and_get_the_list_of_results()), 0,
                            "The search result is empty")
        first_result = self.all_google_page._wait_and_get_the_list_of_results()[0]
        self.assertIn(search_phrase, first_result,
                      "In search result for {} there are not results".format(search_phrase))

    def tearDown(self):
        self.driver.get("https://www.google.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
