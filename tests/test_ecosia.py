from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_find():
    browser.open('https://www.ecosia.org/')

    s('[name=q]').type('yashaka selene').press_enter()
    ss('.result').first.click()

    ss('[href="/yashaka/selene"]').should(have.size(3))
