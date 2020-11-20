import pytest
import os
import subprocess
from selenium import webdriver
from ts.xmarie_driver import XmarieDriver
import psutil

@pytest.fixture
def xmarie_driver():
    d = XmarieDriver(webdriver.Chrome())
    yield d
    d.close()

@pytest.fixture(scope='session', autouse=True)
def backend_server():
    path_to_server_app = os.getenv('XMARIE_SERVER_PATH')
    p = subprocess.Popen(['bash', 'runserver.sh'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, start_new_session=True)
    yield
    for proc in psutil.process_iter():
        if proc.name() == "python":
            proc.kill()
