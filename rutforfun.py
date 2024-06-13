from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import simpledialog

def get_credentials():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    rut = simpledialog.askstring("Input", "Please enter your RUT number:", parent=root)
    password = simpledialog.askstring("Input", "Please enter your Password:", show='*', parent=root)
    return rut, password

def check_page_load(driver):
    return driver.execute_script("return document.readyState;") == "complete"

def login(rut, password):
    driver = webdriver.Chrome()
    driver.get("https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/home/productos-/cuentas/cuentarut.html#/login")

    # Check if the page is fully loaded
    while not check_page_load(driver):
        time.sleep(1)  # Wait for the page to load

    # Use WebDriverWait to wait for the elements to be interactable
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to be clickable
    rut_input = wait.until(EC.element_to_be_clickable((By.ID, 'rut')))
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'pass')))
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'btnLogin')))

    rut_input.send_keys(rut)
    password_input.send_keys(password)
    login_button.click()

    time.sleep(5)  # Wait for page to load, adjust time as necessary
    driver.quit()

rut, password = get_credentials()

# Perform action 10 times
for _ in range(10):
    login(rut, password)
    time.sleep(5)  # Wait 5 seconds between each login

time.sleep(300)  # Wait 5 minutes

# Perform action 5 more times
for _ in range(5):
    login(rut, password)
    time.sleep(5)  # Wait 5 seconds between each login