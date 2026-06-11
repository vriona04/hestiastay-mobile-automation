from utils.base_page import BasePage


class WifiPage(BasePage):

    def verify_wifi_card(self):
        page = self.driver.page_source

        assert "Wi-Fi Details" in page
        assert "Airtel" in page
        assert "Wifi" in page