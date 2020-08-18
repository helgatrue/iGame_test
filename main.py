from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.igame.com/eye-test/index-en.html")
    driver.find_element_by_id("colortest")
    driver.maximize_window()

    for i in range(45):
        elem = driver.find_element_by_class_name("thechosenone")
        elem.click()

    driver.save_screenshot("eyetest.png")
    driver.close()


if __name__ == '__main__':
    main()
