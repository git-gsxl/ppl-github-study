# coding=utf-8
def get_url(s):
    d_url = 'http://www.risecenter.com/plus/school.php?a=cityview&city=404'
    res = s.get(d_url)
    res_data1 = re.findall('href="(.+?)">', res.text)
    res_data = []
    for i in res_data1:
        if 'target' in i:
            url = re.findall('cityview&city=(.+?)" target="_parent', i)
            res_data.append(url)
    resq =(k for i in res_data for k in i)

    return [resq]

def wirte_result(s, report_path):
    '''判断是否需要新建表格'''
    res_excel = os.path.isfile('Excel.xls')
    if res_excel is False:
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Sheet1')
        worksheet.write(0, 0, label='校区')
        worksheet.write(0, 1, label='联系电话')
        worksheet.write(0, 2, label='联系地址')
        workbook.save('Excel.xls')
    count = 0
    for i in get_url(s)[0]:
        url = 'http://www.risecenter.com/plus/school.php?a=cityview&city=' + i
        res = s.get(url).text
        res_data = re.findall('><strong>(.+?)</strong><br>联系电话：(.+?)<br>联系地址：(.+?)</a></p>', res)

        for i in res_data:
            count += 1
            excel = copy(open_workbook(report_path,
                                       formatting_info=True))
            table = excel.get_sheet('Sheet1')
            table.write(count, 0, i[0])
            table.write(count, 1, i[1])
            table.write(count, 2, i[2])
            print(count, '校区：%s,联系电话：%s，地址：%s' % (i[0], i[1], i[2]))
            excel.save(report_path)  # 保存并覆盖文件

if __name__ == '__main__':
    import re, requests, xlwt, os
    from xlrd import open_workbook
    from xlutils.copy import copy

    s = requests.session()
    res = wirte_result(s, os.path.join(os.getcwd(), 'Excel.xls'))
    # os.system(os.path.join(os.getcwd(), 'Excel.xls'))

