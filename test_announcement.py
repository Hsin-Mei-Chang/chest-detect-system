from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# 啟動瀏覽器
driver = webdriver.Chrome()

# 打開頁面
driver.get("https://730e-2001-b011-e606-5d96-246e-262a-9cb1-5578.ngrok-free.app/login")
time.sleep(2)

# 點擊 Visit Site 按鈕
visit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Visit Site')]")
visit_button.click()

# 顯式等待直到登錄表單出現
wait = WebDriverWait(driver, 10)

# 找到 username 輸入框並輸入內容
username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.clear()  # 清空輸入框，防止有預設值
username_input.send_keys("B")  # 替換成實際的使用者名稱

# 找到 password 輸入框並輸入內容
password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.clear()  # 清空輸入框
password_input.send_keys("B1234567")  # 替換成實際的密碼

# 登入按鈕點擊
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()


# 等待並滾動頁面確保按鈕可見
submit_button_next = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-next")))
submit_button_prev = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-prev")))

for i in range(3):
    # 點擊下一頁按鈕
    submit_button_next.click()
    time.sleep(1)  # 等待頁面過渡效果
for i in range(3):
    # 點擊上一頁按鈕
    submit_button_prev.click()
    time.sleep(1)  # 等待頁面過渡效果

# 可以加上時間等待，確保操作能完成
time.sleep(5)

# 關閉瀏覽器
driver.quit()
