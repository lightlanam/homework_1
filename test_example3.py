import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 


@pytest.fixture
def driver(request):
    wd=webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example3(driver):
    driver.get("http://www.google.com")
    driver.implicitly_wait(10) # seconds
    driver.find_element_by_class_name("MiYK0e").click()
    driver.find_element_by_id("K72").click()
    time.sleep(10)