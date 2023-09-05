from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.cathaybk.com.tw/cathaybk")
try :
    driver.implicitly_wait(1)
    layer_1 = driver.find_elements(By.CLASS_NAME,"cubre-o-menuLinkList__content")
    layer_1 = layer_1[1].find_elements(By.TAG_NAME,"a")
    print(f'共有 {len(layer_1)} 項！')
    # select = driver.find_element(By.XPATH, "//div[@class='cubre-o-menu__item']")
    # ActionChains(driver).move_to_element(select).perform()
    # driver.get_screenshot_as_file("./image/test_2.png")
finally:
    driver.close()