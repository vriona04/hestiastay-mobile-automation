from utils.base_page import BasePage


class EmergencyContactPage(BasePage):

    def verify_emergency_contact(self):
        page = self.driver.page_source

        assert "Emergency Contact" in page
        assert "Contact Name" in page
        assert "Contact Phone" in page