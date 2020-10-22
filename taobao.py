# 导入selenium包
import time
from selenium import webdriver

# 打开浏览器: Chrome的C大写的！！ 浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("https://www.taobao.com/")

# 手动扫描
time.sleep(10)
driver.get("https://www.taobao.com/")

driver.find_element_by_xpath('//*[@id="q"]').send_keys("摄像头")
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()


# 结果页面
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[1]/div/div[1]').click()
# 商品详情页面
driver.implicitly_wait(10)

driver.switch_to_window(driver.window_handles[-1])

# 选取商品规则
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[3]/a/span').click()
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li[2]/a/span').click()
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[3]/dd/ul/li[2]/a/span').click()

# 点击购买
driver.find_element_by_xpath('//*[@id="J_LinkBuy"]').click()

driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a').click()

# 输入支付宝
time.sleep(15)
# driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/span').click()
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[1]/b').send_keys("0")
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[2]/b').send_keys("0")
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[3]/b').send_keys("0")
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[4]/b').send_keys("0")
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[5]/b').send_keys("0")
driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[6]/b').send_keys("0")

driver.find_element_by_xpath('//*[@id="J_authSubmit"]').click()