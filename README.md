# TODO Application - Manual & Automated Testing

## 🎯 Aim

To develop a simple TODO application and test its functionality manually and using Selenium automation.

---

## 🛠 Tools Used

* **Frontend:** HTML, CSS, JavaScript
* **Testing & Automation:** Python, Selenium

---

## ✅ TODO App Features

* Add Task
* Delete Task
* Mark Task as Done (toggle complete)

---

## 🔎 Manual Testing Procedure

### 1. Add Item:

* Enter task name in input field.
* Click **Add** button.
* ✅ Verify task appears in the list.

### 2. Delete Item:

* Click **Delete** button next to a task.
* ✅ Verify task is removed.

### 3. Mark as Done:

* Click on the task name.
* ✅ Verify style changes (e.g., strikethrough or color change).

---

## 🤖 Selenium Automated Testing

### Requirements

* Python 3.x
* Selenium (`pip install selenium`)
* ChromeDriver (must be in PATH)

### Setup

```bash
python test_todo_app.py
```

### Test Scenarios

1. **Open the Application**
2. **Add Task**: Type a task and click Add ➡ Check task is visible
3. **Mark as Done**: Click task ➡ Check for class/style change
4. **Delete Task**: Click delete button ➡ Task should disappear

### Sample Code Snippet

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("file:///path-to-your-local/todo.html")  # Update path accordingly

# Add Task
task_input = driver.find_element(By.ID, "task-input")
task_input.send_keys("Test Task")
driver.find_element(By.ID, "add-btn").click()

# Verify
assert "Test Task" in driver.page_source

# Mark as Done
driver.find_element(By.CLASS_NAME, "task-text").click()

# Delete
driver.find_element(By.CLASS_NAME, "delete-btn").click()

# Close
driver.quit()
```

---

## 📋 Outcome

* All functionalities manually verified.
* Selenium automation validates key operations.
* UI is responsive and functional.

---


---

## 💡 Suggestions for Extension

* Store tasks in localStorage.
* Add edit functionality.
* Add task due date.
* Include filters: All / Active / Completed

---

**Author:** Thaarugeshwari KS

**Status:** ✅ Completed
