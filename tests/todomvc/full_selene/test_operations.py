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
    ss('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()

    # THEN
    ss('#todo-list>li').filtered_by(have.css_class('completed')) \
        .should(have.exact_texts('b'))
    ss('#todo-list>li').filtered_by(have.no.css_class('completed')) \
        .should(have.exact_texts('a', 'c'))
