from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(400, 800)
driver.get("https://www.cathaybk.com.tw/cathaybk")

xpath = driver.find_element(By.XPATH, "/html/body")
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", xpath, "class", "is-loaded is-burgerOpen is-menuOpen")

xpath = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]")
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", xpath, "class", "cubre-o-menu__item is-L1open")

xpath = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]")
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", xpath, "style", "display:block;")

xpath = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]")
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", xpath, "class", "cubre-o-menuLinkList__item is-L2open")

layer_1 = driver.find_elements(By.CLASS_NAME,"cubre-o-menuLinkList__content")
layer_1 = layer_1[1].find_elements(By.TAG_NAME,"a")
print(f'共有 {len(layer_1)} 項！')

time.sleep(1)
driver.get_screenshot_as_file("./image/test_2.png")
driver.quit()

