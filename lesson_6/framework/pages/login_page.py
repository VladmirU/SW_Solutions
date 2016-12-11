from locators import locator

def login(user):
    print 'In {locator_name} field input value {name}.'.format(locator_name = locator.USER_NAME_FIELD, name = user['Name'])
    print 'In {locator_password} field input value {password}.'.format(locator_password=locator.PASSWORD_FIELD, password=user['Password'])
    print  'Click {button}.'.format(button = locator.SUBMIT_BUTTON)