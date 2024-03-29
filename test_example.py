import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

@pytest.fixture
def driver(request):
    wd=webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").submit()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Пошук Google"))
    time.sleep(10)
    
    

   