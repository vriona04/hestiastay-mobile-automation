from utils.base_page import BasePage


class SupportPage(BasePage):

    def verify_create_ticket_form(self):

        page = self.driver.page_source

        assert (
            "Create Ticket" in page
            or "Need Help?" in page
        )

    def save_debug(self, name):

        with open(
            f"screenshots/{name}.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(self.driver.page_source)