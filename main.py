from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import username, password
import time

class IgBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com/")
        time.sleep(3)

        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)

        password_field = driver.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(8)

        notifsDodge = driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]")
        notifsDodge.click()

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        for i in range(1, 20):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if '/p/B-' in href]

        for idx, pic_href in enumerate(pic_hrefs):
            driver.get(pic_href)

            try:
                if len(driver.find_elements_by_css_selector('._97aPb + div > section > span > button.wpO6b > svg[aria-label="Me gusta"]')) >= 1:
                    if len(driver.find_elements_by_xpath("//header//a[(text() = 'im_andrevital')]")) <= 0:
                        driver.find_element_by_class_name("wpO6b").click()
                        time.sleep(18)
                    else: time.sleep(2)
                else: time.sleep(2)
            except Exception as e: time.sleep(2)

myBot = IgBot(username, password)
myBot.login()
myBot.like_photo('audioloveofficial')