from utils.base_page import BasePage

class ProfilePage(BasePage):

    def verify(self):
        assert self.page_contains("My Profile")
        assert self.page_contains("Edit Profile")
        assert self.page_contains("Email Address")
        assert self.page_contains("Phone Number")

    def back(self):
        self.click_a11y("Back")