from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_complete_todo():
    # GIVEN
    browser.open('http://todomvc.com/examples/emberjs/')
    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()
    ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # WHEN
    s('#todo-list>li:nth-of-type(2) .toggle').click()

    # THEN
    ss('#todo-list>li.completed').should(have.exact_texts('b'))
    ss('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))
