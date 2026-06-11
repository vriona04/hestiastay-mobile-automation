from utils.base_page import BasePage


class ProfileDetailsPage(BasePage):

    def verify_profile_screen(self):
        page = self.driver.page_source

        assert (
            "Profile" in page
            or "mounika Reddy" in page
            or "Room 105" in page
        ), "Profile screen not found"