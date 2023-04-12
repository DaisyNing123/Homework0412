import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class test_Search():
  def __init__(self):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_search(self):
    self.driver.get("https://www.lagou.com/")
    self.driver.maximize_window
    time.sleep(2)
    #Select localtion window pops up
    result = self.driver.find_element(By.ID, "changeCityBox")
    if result:
      self.driver.find_element(By.ID, "cboxClose").click()
    else:
      pass
    #Search text
    self.driver.find_element(By.ID, "search_input").click()
    self.driver.find_element(By.ID, "search_input").send_keys("字节跳动")
    self.driver.find_element(By.ID, "search_input").send_keys(Keys.ENTER)
    time.sleep(3)

    #Actual result
    res = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/h3/a")
    #Expected result
    assert res.text == "字节跳动"
  
test = test_Search()
test.test_search()
test.teardown_method()
