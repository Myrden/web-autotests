from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()

    # tasks should be "a", "b", "c"
    ss('#todo-list>li').should(have.texts('a', 'b', 'c'))

    # toggle b
    s('.todo-list>li:nth-child(2)').should(have.text('b'))
    s('.todo-list>li:nth-child(2) .toggle').click()

    # completed tasks should be b
    s('.todo-list>li:nth-child(2)').should(have.text('b'))
    s('.todo-list>li:nth-child(2)').should(have.css_class('completed'))

    # active tasks should be a
    s('.todo-list>li:nth-child(1)').should(have.text('a'))
    s('.todo-list>li:nth-child(1)').should(have.no.css_class('completed'))

    # active tasks should be c
    s('.todo-list>li:nth-child(3)').should(have.text('c'))
    s('.todo-list>li:nth-child(3)').should(have.no.css_class('completed'))
