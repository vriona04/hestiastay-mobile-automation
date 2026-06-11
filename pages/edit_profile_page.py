from utils.base_page import BasePage


class EditProfilePage(BasePage):

    def verify_edit_profile_screen(self):
        page = self.driver.page_source

        assert (
            "Edit Profile" in page
            or "Full Name" in page
            or "Email Address" in page
            or "Phone Number" in page
        ), "Edit Profile screen not found"