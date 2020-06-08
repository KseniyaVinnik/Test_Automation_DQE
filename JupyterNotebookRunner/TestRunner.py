import sys
import time
import selenium
from selenium import webdriver


def test_runner():
    try:
        browser = webdriver.Chrome()
        browser.get('https://projectby.trainings.dlabanalytics.com/kvinnik06/')
    except selenium.common.exceptions.InvalidArgumentException:
        sys.exit('Can\'t open URL')

    try:
        button_epam_sso = browser.find_element_by_css_selector('#zocial-epam-idp > span')
        button_epam_sso.click()
    except selenium.common.exceptions.NoSuchElementException:
        sys.exit('Can\'t find the element to log in')

    browser.implicitly_wait(10)

    try:
        choose_notebook = browser.find_element_by_css_selector('#notebook_list > div:nth-child(2) > div > a')
        choose_notebook.click()
    except selenium.common.exceptions.NoSuchElementException:
        sys.exit('Can\'t find the notebook')

    browser.implicitly_wait(60)

    browser.switch_to.window(browser.window_handles[1])

    try:
        cell = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/div/div/div/ul/li[5]/a')
        cell.click()
    except selenium.common.exceptions.NoSuchElementException:
        sys.exit('Can\'t find the cell menu')

    try:
        run_cell = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div/div/div/ul/li[5]/ul/li[4]/a")
        run_cell.click()
    except selenium.common.exceptions.NoSuchElementException:
        sys.exit('Can\'t find "Run All" option')

    time.sleep(20)

    browser.quit()
    print("Please follow the link to find DQ results \n"
          "https://projectby.trainings.dlabanalytics.com/kvinnik06/")


if __name__ == "__main__":
    test_runner()
