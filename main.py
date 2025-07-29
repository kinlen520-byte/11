from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://your-company-portal.com/meeting/reserve")

    Select(driver.find_element(By.ID, "roomDropdown")).select_by_visible_text("会议室A")
    driver.find_element(By.ID, "dateInput").send_keys("2025-08-01")
    Select(driver.find_element(By.ID, "timeSlot")).select_by_visible_text("10:00 - 11:00")
    driver.find_element(By.ID, "submitBtn").click()

    print("Booking submitted successfully")
    time.sleep(3)
    driver.quit()

except Exception as e:
    print("Something went wrong:", str(e))
