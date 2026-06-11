from utils.base_page import BasePage
import time

class LeavePage(BasePage):

    def select_reason(self):
        self.click_a11y("Going Home")
        time.sleep(2)

    def confirm_leave(self):
        for _ in range(3):
            if self.page_contains("Confirm Leave"):
                break
            self.scroll_down()

        self.click_a11y("Confirm Leave")
        time.sleep(4)

    def verify_active_leave(self):
        self.go_home()
        assert self.page_contains("You are on Leave")
        assert self.page_contains("Active")

    def end_leave(self):
        self.go_home()
        self.click_a11y("End Leave & Return")
        time.sleep(4)