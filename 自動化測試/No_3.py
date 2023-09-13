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

time.sleep(2)
card = driver.find_element(By.ID, 'lnk_Link')
card.click()

xpath = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/div/div/div/div[1]/div")
driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", xpath, "class", "cubre-m-anchor__slider swiper swiper-container-initialized swiper-container-horizontal swiper-container-free-mode swiper-container-android is-pageEnd")

driver.execute_script("window.scrollBy(0, 3850);")

anchor = driver.find_elements(By.CLASS_NAME,"cubre-o-anchorBlock")
div = anchor[5].find_elements(By.CLASS_NAME,"cubre-o-slide__item")
now_size = 0
size = 465
for i in range(len(div)):
    style = anchor[5].find_element(By.CLASS_NAME, "swiper-wrapper")
    js = f"transform: translate3d({now_size}px, 0px, 0px);transition-duration: 0ms;"
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", style, "style", js)
    time.sleep(1)
    now_size -= size
    driver.get_screenshot_as_file(f"./image/card/card_{i+1}.png")

time.sleep(3)
driver.quit()

