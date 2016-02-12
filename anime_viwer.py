# coding: utf-8
from selenium import webdriver
import time

if __name__ == "__main__":
    keyword = raw_input("作品名の入力\n__>")

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://anipo.jp/")

# 作品名検索
    d_title = driver.find_element_by_class_name("search-text")
    d_title.send_keys(keyword.decode('utf-8'))
    d_title.submit()

# 詳細リンクに飛ぶ
    list = driver.find_element_by_css_selector('.search-list a')
    print "*", list.text
    list.click()
# 詳細リンク
    driver.execute_script('window.scrollTo(0, 1000)')
    time.sleep(3)
    anitube_link = driver.find_element_by_css_selector('.d1 li:nth-child(2) a') #d~ ~話
    anitube_link.click()

# window切り替え
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
# 再生開始
    driver.find_element_by_css_selector('.mainBox li a').click() #d~ ~話

#driver.close()
