from selene import browser, have, be

def test_duckduckgo_search():
    browser.open('https://duckduckgo.com')
    browser.element("[placeholder='Поиск без отслеживания']").should(be.blank).type('qa.guru').press_enter()
    browser.element('div h2 a span').should(have.text('Курсы тестировщиков — обучение тестированию онлайн'))