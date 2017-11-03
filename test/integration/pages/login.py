# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Login page locators and functions."""

from pypom import Page
from selenium.webdriver.common.by import By

from pages.home import Home


class Login(Page):
    """Set up the login page locators and functions."""

    _password_locator = (By.NAME, 'password')
    _confirm_password_locator = (By.NAME, 'confirmPassword')
    _continue_locator = (By.CSS_SELECTOR, 'button.button__button___267m4')

    def wait_for_page_to_load(self):
        """Page load wait."""
        self.wait.until(
            lambda s: any(s.find_elements(*self._password_locator)))
        return self

    def login(self, password):
        """Login to lockbox."""
        self.find_element(*self._password_locator).send_keys(password)
        self.find_element(*self._confirm_password_locator).send_keys(password)
        window_handles = self.selenium.window_handles
        self.find_element(*self._continue_locator).click()
        # FIXME: after logging in a new tab is opened with the home page. This
        # waits for the new tab and then switches focus to the last handle.
        # We should do something smarter here, or Lockbox should reuse the same
        # tab (arguably a better user experience too).
        self.wait.until(lambda s: len(s.window_handles) > len(window_handles))
        self.selenium.switch_to.window(self.selenium.window_handles[-1])
        return Home(self.selenium).wait_for_page_to_load()
