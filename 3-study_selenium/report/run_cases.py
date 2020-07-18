'''
这个是优化版执行所有用例发送测试报告，四个步骤
第一步加载用例
第二步执行用例
第三步获取最新测试报告
第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）
'''
# coding=utf-8
import unittest, time, os, HTMLTestRunner       # HTMLTestRunner生成html报告
import smtplib                                  # 负责发送邮件
from email.mime.text import MIMEText            # 负责构造邮件的正文
from email.mime.multipart import MIMEMultipart

report_name = u'API自动化测试报告.study_html'         # 报告名称
report_title = u'API自动化测试'                  # 报告title名称
report_ename = 'api_report.study_html'                # 附件名称

# 当前脚本所在文件真实路径zentao
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def add_case(caseName='cases', rule='test*.py'):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)

    # 如果不存在这个cases文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(caseName)

    # 定义 discover 方法的参数，返回测试用例列表文件名
    discover = unittest.defaultTestLoader.discover(case_path,
    pattern=rule,
    top_level_dir=None)
    return discover

def run_case(all_case, reportName='report'):
    '''第二步：执行所有的用例, 把结果写入测试报告'''
    report_Folder = os.path.join(cur_path, "report")
    if not os.path.exists(report_Folder):os.mkdir(report_Folder)    # report文件夹，没有的话自动创建一个

    report_path = os.path.join(report_Folder, report_name)  # 测试报告名称
    print('report path:%s' % report_path)

    # 加载所有用例，写入测试报告，生成
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, retry=0)
    # 调用 add_case 函数返回值
    runner.run(all_case)    # 执行
    fp.close()

def get_report_html(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)     # 获取report目录下的最新测试报告
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： '+lists[-1])

    report_file = os.path.join(report_path, lists[-1])  # 找到最新生成的报告文件
    return report_file

def get_report_xls(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)     # 获取report目录下的最新测试报告
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： '+lists[-2])

    report_file = os.path.join(report_path, lists[-2])  # 找到最新生成的报告文件
    return report_file


def send_mail(sender, pwd, receiver, smtpserver, report_file, port):
    '''发送最新的测试报告内容'''

    with open(report_file, "rb") as f:
        mail_body = f.read()

    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='study_html', _charset='utf-8')
    msg['Subject'] = report_title+u'报告'
    msg["from"] = sender
    if isinstance(receiver, str):
        msg["to"] = receiver
    if isinstance(receiver, list):
        msg["to"] = ','.join(receiver)

    # 加上时间戳，显示报告的内容
    time.strftime('%a, %d %b %Y %H_%M_%S %z')
    msg.attach(body)

    # 邮箱添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= %s' % report_ename
    msg.attach(att)

    try:
        smtp = smtplib.SMTP()       # 登录邮箱
        smtp.connect(smtpserver)    # 连接邮箱服务器
        smtp.login(sender, pwd)     # 用户名密码

    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, pwd)                         # 登录
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('测试报告电子邮件已发送！')


if __name__ == "__main__":
    all = add_case()   # 加载用例
    run_case(all)      # 执行用例

    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, 'report')  # 这个文件夹下
    report_file = get_report_html(report_path)      # 获取最新测试报告路径

    # 邮箱配置
    sender = '772262624@qq.com'
    pwd = 'rlcfmsgcccgrbejj'  # SSL授权码登录
    smtp_server = 'smtp.qq.com'
    port = 465
    receiver = ['772262624@qq.com']  # 可多个邮箱传list对象

    from selenium import webdriver
    # driver = webdriver.Chrome()        # 浏览器正常模式

    option = webdriver.ChromeOptions()   # 浏览器静默模式
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)

    html_path = os.path.join(cur_path, 'report', report_name)  # 获取报告文件目录
    driver.get(html_path)  # 打开html测试报告

    from project_lyl.mjj_app.common.base import Base
    b = Base(driver)
    loc_Failure = ('xpath', '/study_html/body/div[2]/p[3]/span[2]')
    loc_Error = ('xpath', '/study_html/body/div[2]/p[3]/span')
    t1 = b.get_text(loc_Failure)
    t2 = b.get_text(loc_Error)

    # 判断 测试报告 是否有Failure、Error、空值
    if (t1 or t2) in ('Failure', 'Error', ''):
        # pass      # 4.最后一步发送报告 注释掉就不发邮件
        send_mail(sender, pwd, receiver, smtp_server, report_file, port)
    else:
        print('用例全部通过，不需要发送邮件')
    driver.quit()
