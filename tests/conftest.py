import pytest
from selenium import webdriver
from ts.xmarie_driver import XmarieDriver

@pytest.fixture
def xmarie_driver():
    d = XmarieDriver(webdriver.Chrome())
    yield d
    d.close()

