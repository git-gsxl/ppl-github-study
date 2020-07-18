import re, requests, time, os

def get_chatper_data(chatper_url):
    response = requests.get(chatper_url)
    response.encoding = 'utf-8'
    html = response.text

    #  如果 re 能提取需要的数据就返回真实存在数据，否则返回错误！
    try:
        chatper_data = re.findall(r'<div id="content">(.*?)</div>', html, re.S)[0]
        # 去掉干扰字符
        chatper_data = chatper_data.replace('<br/><br/>', '')
        chatper_data = chatper_data.replace('&nbsp;', '')
        return chatper_data
    except:pass


def get_chatper_title(nover_url):
    response = requests.get(nover_url)
    response.encoding = "utf-8"
    html = response.text
    chatper_title = re.findall(r'<dd><a href="(.*?)">(.*?)<',html,re.S)
    return chatper_title

def get_text(count=0,res=10,ret=10,sleep=60):
    '''
    count = 0       执行次数统计
    res = 10        初始化10次进行时间等待
    ret = 10        每执行10次进行时间等待
    sleep = 60      等待时间
    '''

    url = "http://www.biquku.la/3/3516/"
    title = get_chatper_title(url)
    try:
        os.remove('重生之超级公子.txt')
    except:
        pass

    for chatper in title:
        get_url = 'http://www.biquku.la/3/3516/%s' % chatper[0]
        chatper_data = get_chatper_data(get_url)
        if chatper_data:
            count += 1
            if count > res :
                print('正在等待%sS后继续！！！' % sleep)
                time.sleep(sleep)
                res += ret

            with open('重生之超级公子.txt', 'a', encoding='utf-8')as f:
                f.write(chatper[1] + '\n')
                f.write(chatper_data + '\n' + '\n')
            print(chatper)
        else:
            data = ('发生错误的：' + get_url)
            print(data)

if __name__ == '__main__':
    get_text()
