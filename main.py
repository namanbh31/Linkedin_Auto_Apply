from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_executable_path = r""#Path for chrome driver
options = webdriver.ChromeOptions()

options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_executable_path)  # , options=options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location="
           "London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
# To click on the Sign button
time.sleep(3)
sign_in = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")
sign_in.click()
# To login
time.sleep(1)
login = driver.find_element(By.ID, 'username')
login.send_keys("")# Your email for login

password = driver.find_element(By.ID, "password")
password.send_keys("")# your password for login

submit = driver.find_element(By.CSS_SELECTOR,"button.btn__primary--large").send_keys(Keys.ENTER)


def close_chat_box():
    # To close the chat window
    chat_popup_close = driver.find_element(By.CSS_SELECTOR,
        '#msg-overlay > div.msg-overlay-list-bubble.ml4 > header > section.msg-overlay-bubble-header__details.flex-row.align-items-center.ml1')
    chat_popup_close.click()


def save_and_follow():
    # To click on the save button
    save = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
    save.click()

    # To scroll to the bottom of the page
    # job_detail = driver.find_element_by_class_name("jobs-search__right-rail")
    # job_detail.click()
    # html = driver.find_element_by_tag_name("html")
    # html.send_keys(Keys.END)

    time.sleep(5)
    # follow = driver.find_element_by_css_selector("button.follow")
    # follow.click()


# close_chat_box()

time.sleep(30)
def get_job():

    close_chat_box()
    job_options = [job.get_attribute('href') for job in driver.find_element(By.CSS_SELECTOR,
        "div.jobs-search-two-pane__wrapper  ul.jobs-search-results__list li a.job-card-container__link.job-card-list__title")]
    for job in job_options:
        driver.get(job)
        time.sleep(5)
        save_and_follow()
        time.sleep(5)


get_job()
# driver.quit()
