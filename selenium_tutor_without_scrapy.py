from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
# Don't automatically close browser
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get('https://www.iana.org/domains/reserved')


# `find_element_by_tag_name` new version not work
h1 = browser.find_element(By.TAG_NAME, 'h1')
print(h1.text)

iana_table = browser.find_element(By.CLASS_NAME, "iana-table")
print(iana_table.text)

arpa_table = browser.find_element(By.ID, "arpa-table")
print(arpa_table.text)

td = browser.find_element(By.XPATH, "//table[@id='arpa-table']/tbody/tr[1]/td[1]")
print(td.text)

link = browser.find_element(By.LINK_TEXT, 'RFC 2606')
link.click()
