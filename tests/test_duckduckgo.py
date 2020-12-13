from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_search():
    browser.open('https://duckduckgo.com/')

    s('[name=q]').type('yashaka selene').press_enter()
    ss('.result__body').first.click()

    ss('[href="/yashaka/selene"]').should(have.size(3))
