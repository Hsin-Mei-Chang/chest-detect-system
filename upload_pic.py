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

# 等待網頁加載完成
wait = WebDriverWait(driver, 10)

submit_button1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '疾病辨識')]")))
submit_button1.click()

try:
    # 上傳圖片
    upload_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    upload_element.send_keys("C:/Users/user/OneDrive/桌面/胸腔辨識/00028174_000.png")

    # 點擊辨識按鈕
    submit_button = driver.find_element(By.ID, "predict-button")
    driver.execute_script("arguments[0].click();", submit_button)

    # 加入延遲，確保結果返回
    time.sleep(5)  # 等待5秒

    # 查找結果
    result_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "detect-disease"))
    )
    
    # 列印出 result_element 的文本
    print(result_element.text)
    
    # 驗證結果是否正確
    assert "辨識結果: Infiltration" in result_element.text

    data_saved_button = driver.find_element(By.CLASS_NAME, "data-saved")
    driver.execute_script("arguments[0].click();", data_saved_button)
finally:
    driver.quit()
    print("Test Finished")
