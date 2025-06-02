from selene import browser, have, be

# Positive test
def test_duckduckgo_search():
    browser.open('https://duckduckgo.com')
    browser.element("[placeholder='Поиск без отслеживания']").should(be.blank).type('qa.guru').press_enter()
    browser.element('div h2 a span').should(have.text('Курсы тестировщиков — обучение тестированию онлайн'))

#Negative test
def test_duckduckgo_search():
    browser.open('https://duckduckgo.com')
    browser.element("[placeholder='Поиск без отслеживания']").should(be.blank).type('khpfsrmnhgdde').press_enter()
    browser.element('div h2 a span').should(have.text('По запросу khpfsrmnhgdde ничего не найдено.'))