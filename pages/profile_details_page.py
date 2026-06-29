from utils.base_page import BasePage


class ProfileDetailsPage(BasePage):

    def verify_profile_screen(self):
        page = self.driver.page_source

        assert (
            "My Profile" in page
            or "Edit Profile" in page
            or "Personal Information" in page
            or "Email Address" in page
            or "Phone Number" in page
            or "Profile" in page
        ), "Profile screen not found"

        print("PROFILE DETAILS PAGE VERIFIED")