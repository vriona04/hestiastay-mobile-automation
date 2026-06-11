from utils.base_page import BasePage


class PaymentHistoryPage(BasePage):

    def verify_payment_history(self):
        page = self.driver.page_source

        assert "Payment History" in page
        assert "Rent Payment" in page
        assert "PAID" in page