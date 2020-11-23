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
    cmd = [f'{path_to_server_app}/env/bin/python', '-m', 'flask', 'run']
    p = subprocess.Popen(
        cmd, 
        cwd=path_to_server_app,
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.STDOUT, 
        start_new_session=True,
    )
    yield
    p.kill()