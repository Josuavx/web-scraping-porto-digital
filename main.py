from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(browser, 15)

browser.get("https://www.google.com.br")

search_input = browser.find_element(By.NAME, "q")

search_input.send_keys('Porto Digital')

search_input.send_keys(Keys.RETURN)

browser.find_element(By.XPATH, "//h3[text()='Porto Digital - Recife']").click()

browser.find_element(By.XPATH, '//a[@class="header-link" and @href="/noticias"]').click()

wait.until(EC.visibility_of_element_located(By.XPATH, '//ul[@class="columnCount2"]'))
elemento_scroll = browser.find_element(By.XPATH, '//ul[@class="columnCount2"]')

print(elemento_scroll)
browser.execute_script("arguments[0].scrollIntoView();", elemento_scroll)

sleep(5)
lista_noticias = browser.find_elements(By.XPATH, '//ul[@class="columnCount2"]/*')

print(f'Lista: {lista_noticias}')
for noticia in lista_noticias:
    classificacao = noticia.find_element(By.XPATH, './/div[@class="news-body"]')
    print(classificacao.get_attribute('textContent'))

sleep(100)