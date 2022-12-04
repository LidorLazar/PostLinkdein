import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('./post.txt', encoding="utf-8") as f:
    file = f.read()
# line 7-10 open the chrome browser and get the Linkedin.
driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.linkedin.com/'
driver.get(url)

# line 13-16 click on username/email and password input and put the my paramers
email = driver.find_element('xpath', "//input [@name = 'session_key']")
password = driver.find_element('xpath', "//input [@name = 'session_password']")
email.send_keys('')# Write between the apostrophes your email
password.send_keys('') # Write between the apostrophes your password

# line 18-19 click login , line 20 waiting 15 second because of the page loading
click_to_login = driver.find_element('xpath', "//button[@Type = 'submit']")
click_to_login.click()
time.sleep(15)

# line 24-26 search the create post and click him.
click_to_post = driver.find_element("xpath", "//*[@id = 'main']/div[1]/div/div[1]/button")
# click_to_post = driver.find_element("xpath", "(//button[@id='ember29'])[1]")
click_to_post.click()

#line 29-34 click on textbox and take a file text and put it after click post 
time.sleep(3)
input_text = driver.find_element(By.CLASS_NAME, 'ql-editor.ql-blank')
input_text.send_keys(file)

send_post = driver.find_element("xpath", "//div[@class = 'share-box_actions']//span[@class = 'artdeco-button__text']")
send_post.click()

