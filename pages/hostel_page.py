from utils.base_page import BasePage


class HostelPage(BasePage):

    def verify_hostel_details(self):
        page = self.driver.page_source

        assert (
            "Your Hostel" in page
            or "Hestia PG" in page
            or "Room 105" in page
            or "RENT OVERDUE" in page
            or "Need Help?" in page
        ), "Dashboard/hostel section not found"