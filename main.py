import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import json


# 使用QQ登录
def login(config):
    # edge 无头浏览器设置
    EDGE = None
    if not config['show_browser']:
        EDGE = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            # 关键是下面这个
            "ms:edgeOptions": {
                'extensions': [],
                'args': [
                    '--headless',
                    '--disable-gpu',
                    '--remote-debugging-port=9222',
                    'ignore-certificate-errors'
                ]}
        }
    options = Options()
    # 使用的是新版edge，这是edge驱动
    driver = webdriver.Edge(executable_path=config['driver_path'], capabilities=EDGE)
    # driver.minimize_window()
    login_url = "https://pass.hust.edu.cn/cas/login"

    driver.get(login_url)
    wait_for_element_txt('QQ登录', driver)
    qq_login = driver.find_element_by_link_text('QQ登录').click()

    wait_for_element_xpath('//*[@id="ptlogin_iframe"]', driver)
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]'))
    avatar = driver.find_element_by_xpath('//*[@id="qlogin_list"]/a')
    avatar.click()
    print('登录成功')
    sleep(5)
    return driver


def readConfig():
    with open("./config.json") as file:
        return json.load(file)


def wait_for_element_txt(element_txt, browser):
    # print('Waiting for loading:'+element_txt)
    while not browser.find_elements_by_link_text(element_txt):
        sleep(1)


def wait_for_element_xpath(element_xpath, browser):
    # print('Waiting for loading:'+element_txt)
    while not browser.find_elements_by_xpath(element_xpath):
        sleep(1)


def wait_for_element_class(element_class_name, browser):
    # print('Waiting for loading:'+element_class_name)
    while not browser.find_elements_by_class_name(element_class_name):
        sleep(1)


def wait_for_element_tag(element_tag_name, browser):
    while not browser.find_elements_by_tag_name(element_tag_name):
        sleep(1)


def fillForm(browser):
    print('开始填报')
    post_url = 'https://yqtb.hust.edu.cn/infoplus/form/BKS/start'
    browser.get(post_url)
    wait_for_element_txt('下一步', browser)
    # 先填报今天的
    if browser.find_element_by_id('V1_CTRL271').get_property('value') == '已':
        print('今日已填报')
    else:
        print('开始今日填报')
        # 点击 本人今日健康状况填报
        browser.find_element_by_id('V1_CTRL264').click()
        # 点击 下一步
        sleep(1)
        browser.find_element_by_link_text('下一步').click()
        # 点击 下一步 next
        wait_for_element_txt('下一步 Next step', browser)
        browser.find_element_by_link_text('下一步 Next step').click()
        fillTheForm(browser)
        print('今日填报完成')
    print('开始补填报')
    while True:
        # 每次都要重新请求一下
        post_url = 'https://yqtb.hust.edu.cn/infoplus/form/BKS/start'
        browser.get(post_url)
        wait_for_element_txt('下一步', browser)
        # 本人过去健康状况补填报
        # 点击 本人过去健康状况补填报
        browser.find_element_by_id('V1_CTRL265').click()
        sleep(1)
        table = browser.find_element_by_id('groupYQRBList')
        inputs = table.find_elements_by_tag_name('input')
        for i in range(len(inputs)):
            if inputs[i].get_property('value') == '未填报':
                inputs[i + 1].click()
                sleep(1)
                browser.find_element_by_link_text('下一步').click()
                fillTheForm(browser)
                break
        else:
            print('补填报完成')
            break


# 填单个表
def fillTheForm(browser):
    # 填表
    wait_for_element_txt('提交 Submit', browser)
    t = str(random.uniform(36.5, 36.8))[:4]
    browser.find_element_by_id('V1_CTRL164').clear()
    browser.find_element_by_id('V1_CTRL164').send_keys(t)
    sleep(1)
    browser.find_element_by_id('V1_CTRL197').clear()
    browser.find_element_by_id('V1_CTRL197').send_keys('10')
    # 点击提交
    browser.find_element_by_link_text('提交 Submit').click()
    # 点击 好
    wait_for_element_tag('button', browser)
    browser.find_elements_by_tag_name('button')[0].click()
    sleep(3)


def main():
    config = readConfig()
    browser = login(config)
    fillForm(browser)
    browser.quit()


if __name__ == '__main__':
    main()
