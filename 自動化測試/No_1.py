from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cathaybk.com.tw/cathaybk")
try :
    driver.implicitly_wait(5)
    driver.get_screenshot_as_file("./image/test_1.png")
finally:
    driver.close()