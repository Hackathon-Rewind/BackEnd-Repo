from selenium import webdriver

import time

path = '/Users/parkjinhong/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_name('email').send_keys("01088348347")
driver.find_element_by_name('pass').send_keys("105212as@#")

try:
    driver.find_element_by_xpath('//*[@id="u_0_e"]').click()
except:
    try:
        driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="u_0_4"]').click()
        except:
            raise


try:
    driver.find_element_by_xpath('//*[@id="js_g"]').send_keys("asdqwe")
except:
    try:
        driver.find_element_by_xpath('//*[@id="js_5"]').send_keys("qwe")
    except:
        try:
            driver.find_element_by_xpath('//*[@id="js_8"]').send_keys(("qweqwe"))
        except:
            driver.find_element_by_xpath('//*[@id="js_b"]').send_keys(("qweqweq"))

for i in range(9), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    str = f'//*[@id="js_{i}"]'
    try:
        driver.find_element_by_xpath(str).send_keys(str)
        break
    except:
        continue

driver.find_element_by_xpath('//*[@id="js_1b"]/div[2]/div[3]/div[2]/button').click()


