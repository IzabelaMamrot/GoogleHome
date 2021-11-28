
class GoogleImagePage:
    IMG_NAME = 'img'
    IMAGES_NAME = "images"

    def __init__(self, driver):
        self.driver = driver

    def _find_the_image_text_in_google_icon(self):
        return self.driver.find_element_by_class_name("T8VaVe").text

    def _get_the_image_page_url(self):
        return self.driver.current_url
