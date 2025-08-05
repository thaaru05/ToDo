from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

def test_todo_app():
    html_path = os.path.abspath("todo_app.html")
    file_url = "file://" + html_path

    options = Options()
    
    options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Opening local TODO app...")
        driver.get(file_url)
        time.sleep(1)

       
        task_input = driver.find_element(By.ID, "task-input")
        task_input.send_keys("Buy groceries")

        add_btn = driver.find_element(By.XPATH, "//button[text()='Add']")
        add_btn.click()
        time.sleep(1)

        print("Task added.")

        
        done_btn = driver.find_element(By.XPATH, "//li/button[text()='Done']")
        done_btn.click()
        time.sleep(1)

        print("Task marked as done.")

       
        del_btn = driver.find_element(By.XPATH, "//li/button[text()='Delete']")
        del_btn.click()
        time.sleep(1)

        print("Task deleted.")

        print("✅ Automated test completed successfully.")

    except Exception as e:
        print("❌ Test failed:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_todo_app()
