from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if '/p/B-' in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))

        new_Liked = 0
        old_Liked = 0
        own_Pics = 0

        for idx, pic_href in enumerate(pic_hrefs):
            print('Photo ' + str(idx))
            driver.get(pic_href)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                # Like button approach (problem when pic is already liked)
                # # Fixed it by verifying if like button was active
                # # # Added filter to exclude own photos

                if len(driver.find_elements_by_css_selector('._97aPb + div > section > span > button.wpO6b > svg[aria-label="Me gusta"]')) >= 1:
                    # # # print('Not liked yet')
                    if len(driver.find_elements_by_xpath("//header//a[(text() = 'im_andrevital')]")) <= 0:
                        # # # print('Not your photo')
                        driver.find_element_by_class_name("wpO6b").click()
                        # # # new_Liked += 1
                        # # # print('Just liked it! Total likes: ' + str(new_Liked))
                        time.sleep(18)
                    else: 
                        # # # own_Pics += 1
                        # # # print('Your pic / your comment! Count: ' + str(own_Pics))
                        time.sleep(2)
                else: 
                    # # # old_Liked += 1
                    # # # print('Already liked! Count: ' + str(old_Liked))
                    time.sleep(2)                

                # Double tap picture approach (Didn't work) (Couldn't emulate double tap)
                # picture = driver.find_element_by_xpath("//header/following-sibling::div/div[@class='ZyFrc'][@role='button']") 
                # picture.click()
                # picture.click()
            except Exception as e:
                print("Didn't do shit")
                time.sleep(2)

myBot = IgBot("username", "password")
myBot.login();
myBot.like_photo('audioloveofficial')