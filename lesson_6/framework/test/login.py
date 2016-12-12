from dto.user import NAME, PASSWORD
from pages import login_page, home_page
from helpers.navigator import get
from assertions import asserts


def test_login():
    get(login_page)
    asserts.assert_on_login_page()
    login_page.login({'Name':NAME, 'Password':PASSWORD})
    asserts.assert_on_home_page()
    home_page.logout()
    asserts.assert_on_login_page()


if __name__ == "__main__":
    test_login()
