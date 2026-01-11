from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time()
driver = webdriver.Chrome()
driver.get("https://instamatch365.com/")
driver.fullscreen_window()
driver.implicitly_wait(5)

USERNAME = "username"
PASSWORD = "password"

wait = WebDriverWait(driver, 10)

# 1. Ads Pop up close
driver.find_element(By.CLASS_NAME, "clseBtnPar").click()

# 2. Wait for the Login button to appear and click it 
login_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mb-button--login")))
login_btn.click()
# driver.find_element(By.CLASS_NAME, "mb-button--login").click()

# 3. Find username and password fields
user_field = wait.until(EC.element_to_be_clickable((By.ID, "user_login_id")))
pass_field = driver.find_element(By.ID, "passwordId")

# 4. Enter credentials
user_field.send_keys(USERNAME)
pass_field.send_keys(PASSWORD)

# 5. Submit the login form
submit_button = driver.find_element(By.ID, "loginbutton")
submit_button.click()

# 6. Close the pop ups
try:
    popup1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "popup-close")))
    popup1.click()

except:
    popup2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "animCLseBtn")))
    popup2.click()

# 7. Click on the Account icon
acc_btn = wait.until(EC.element_to_be_clickable((By.NAME, "accountsection")))
acc_btn.click()

# 8. Click on the Funds Transfer Menu
driver.find_element(By.LINK_TEXT, "P2P Transfer Funds").click()

# 9. Skip the Pop Up
try:
    skip1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "skip_right_img")))
    skip1.click()
# driver.find_element(By.LINK_TEXT, "P2P Transfer Funds").click()

except:
    pass


amount = driver.find_element(By.CSS_SELECTOR, ".trnfr_select.cls_cr.cls_FundAmount")
payee = driver.find_element(By.CSS_SELECTOR, ".trnfr_select.cls_cr.cls_fundUsername")

amount.send_keys("100")
payee.send_keys("9898989898")

verify = driver.find_element(By.CSS_SELECTOR, ".tnfr_button.mb-button.cl_base.cls_chekUsername.cls_tran_fund")
verify.click()

pass_verify = driver.find_element(By.CSS_SELECTOR, ".trnfr_select.passInp_p2p.cls_password")
pass_verify.send_keys(PASSWORD)

fund_transfer = driver.find_element(By.CSS_SELECTOR, ".tnfr_button.mb-button.cl_base.cls_chekUsername.cls_tran_fund.cls_verify")
fund_transfer.click()

for i in range(20):
    try:
        num = f"{i:06d}"
        input_box = driver.find_element(By.CSS_SELECTOR, ".trnfr_select.cls_otp")
        input_box.clear()
        input_box.send_keys(num)
        
        time.sleep(0.1)
        final_verify = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cls_verify")))
        final_verify.click()
        print(num)
    except Exception as e:
        print(f"Attempt failed: {e}")
        final_verify.click()
        print(num)

    end_time = time.time()    
    print(f"Total runtime: {end_time - start_time:.4f} seconds")

    

time.sleep(5)
driver.close()