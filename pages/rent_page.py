from utils.base_page import BasePage


class RentPage(BasePage):

    def verify_payment_screen(self):
        assert self.page_contains("Payment")