from selene import browser, by, have


# Позитивный тест для поиска
def test_yandex_search_positive(browser_settings):
    browser.open('https://ya.ru')
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('qa.guru').press_enter()
    browser.element(by.xpath("//ul[@id='search-result']")).should(have.text('Курсы тестировщиков — обучение... | '))


# Негативный тест для поиска
def test_yandex_search_negative(browser_settings):
    browser.open('https://ya.ru')
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('khpfsnmnhgdde').press_enter()
    browser.element('.EmptySearchResults > div.EmptySearchResults-Title').should(have.text("Ничего не нашли"))
