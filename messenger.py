import os
import sys
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class instabot:
    def __init__(self, username, password) -> None:
        # Twitter Username and Passwords
        self.username = username
        self.password = password

        # Driver for Selenium
        if sys.platform.startswith('win'):
            driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

       

        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self) -> None:
        # Login URL
        url = 'https://www.instagram.com/accounts/login/'

        # Open the login page
        self.driver.get(url)

        # Sleep for page to load
        self.wait(5, '//*[@id="loginbutton"]')
        print("[+] Page Load Successfull")

        # Username Field
        # username_field = self.driver.find_element_by_name('session[username_or_email]')
        username_field = self.driver.find_element(By.NAME, 'username')
        # Password Field
        password_field = self.driver.find_element(By.NAME, 'password')
        # Login Button
        # login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]')

        # Fill in Username
        username_field.send_keys(self.username)
        # Fill in Password
        password_field.send_keys(self.password)
        # Click Login Button
        # login_button.click()
        password_field.send_keys(Keys.ENTER)
        print("[+] Login Successfull")

    def wait(self, seconds: int, element: str) -> None:
        WebDriverWait(self.driver, seconds).until(
            lambda driver: driver.find_element(By.XPATH, element)
        )
    
    def quite(self) -> None:
        self.driver.quit()
        os.system("taskkill /im chromedriver.exe /f")


def main(username, password):
    bot = instabot(username, password)
    bot.login()
    time.sleep(30)
    bot.quite()

if __name__ == '__main__':
    username = input("Enter your username/email: ")
    password = getpass.getpass("Enter your password: ")
    main(username, password)