from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Chrome()

browser.get(url)

sleep(1)

a = browser.find_element_by_tag_name('a')

for click in range(10):
    ps = browser.find_elements_by_tag_name('p') 
    a.click()
    print(f'Valor do ultimo p {ps[-1].text} valor do click: {click}')
    print(f'Os valores sao iguais {ps[-1].text == str(click)}')

browser.quit()