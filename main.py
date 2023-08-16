import csv
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def write_CSV():

    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sheet-bond-market"]/div/table')))

    data_rows = table.find_elements(By.XPATH, ".//tbody/tr")
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_rows:
            data_cells = row.find_elements(By.XPATH, ".//td")
            data = [cell.text for cell in data_cells]
            writer.writerow(data)
# 创建浏览器实例
driver = webdriver.Edge()
driver.maximize_window()

# 打开链接页面
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
driver.get(url)

driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/select/option[2]').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[6]/div[2]/select/option[2]').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[8]/a[1]').click()
sleep(1)

for i in range(5):
    write_CSV()
    if i < 5:
        driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[4]').click()







