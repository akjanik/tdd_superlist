from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/home/adam/geckodriver/0.11/geckodriver')
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
