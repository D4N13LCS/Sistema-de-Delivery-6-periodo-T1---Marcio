from selenium import webdriver


def test_home_carrega(live_server):

    driver = webdriver.Chrome()

    driver.get(live_server.url)

    assert "Cardápio" in driver.page_source

    driver.quit()