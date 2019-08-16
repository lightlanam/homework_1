import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver(request):
    wd=webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example4(driver):
   driver.get("http://tut.by/")
   driver.implicitly_wait(10)
   time.sleep(10)