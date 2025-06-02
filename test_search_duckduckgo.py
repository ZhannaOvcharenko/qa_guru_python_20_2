from selene import browser, be, have


def test_duckduckgo_search_positive(browser_settings):
    browser.open('https://duckduckgo.com')
    browser.element('[placeholder="Поиск без отслеживания"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('div h2 a span').should(have.text('Курсы тестировщиков - обучение тестированию онлайн'))


def test_duckduckgo_search_negative(browser_settings):
    browser.open('https://duckduckgo.com')
    browser.element('[placeholder="Поиск без отслеживания"]').should(be.blank).type('khpfsnmnhgdde').press_enter()
    browser.element('div h2 a span').should(have.text('По запросу khpfsnmnhgdde ничего не найдено.'))
