from bs4 import BeautifulSoup
import lxml
import requests
import re
import csv
import random
import time
from lxml import etree
from requests.exceptions import RequestException

# -------------------------------输入区域--------------------输入区域---------#
url_of_illness = 'https://haoping.haodf.com/keshi/1010000/daifu_all.htm'  #
illness_name = ""
# ---------------------------------------------------------------------------#


url_all_doctors = []
csv_file_name = illness_name + "医生主页url.csv"


# 访问网页
def get_page(url):
    User_Agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'
    ]

    len_user_agent = len(User_Agent)
    random_num = random.randint(0, len_user_agent - 1)
    user_agent = User_Agent[random_num]

    response = requests.get(url=url, headers={'User-Agent': user_agent})
    response.encoding = 'cp936'

    html = response.text
    status_code = response.status_code

    # 如果限制访问，执行time.sleep，否则不启用
    count = 0
    while status_code == 403:
        response = requests.get(url=url, headers={'User-Agent': user_agent})
        response.encoding = 'cp936'

        html = response.text
        status_code = response.status_code

        count += 1
        time.sleep(count * 0.1)

    return html


# 查找改网页下的医生（每个页面下有30个）
def get_doctor_url_list(html):
    pattern = re.compile('<a href=(.*?)target="_blank" class="blue pernet">访问个人网站.*?</a>')
    url_the_page_list = re.findall(pattern, html)
    for lt in url_the_page_list:
        url_valid = "https:" + eval(lt)
        url_all_doctors.append(url_valid)


# 查看链接时htm还是html，统一格式，防止报错
def check_page_structure(url):
    if url[-1] == 'l':
        return 5
    else:
        return 4


# 定义查找该页面下有多少翻页子页面
def get_pages_number(html):
    select = etree.HTML(html)
    number_string = select.xpath('//a[@class="p_text"]//text()')[0]
    number = re.search('\d+', number_string).group(0)
    number = int(number)
    return number


# 主函数
def main(offset, n):
    url = url_of_illness[:-n] + '_' + str(offset) + '.htm'
    html = get_page(url)
    get_doctor_url_list(html)
    print(len(url_all_doctors))


# 定义写文件
def write_csv(file, url_list, illness_name):
    with open(file, 'a', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ["doctor_url", "Type_of_treatment"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in url_list:
            writer.writerow({"doctor_url": i,
                             "Type_of_treatment": illness_name})


if __name__ == '__main__':
    # 爬取第一页，放入存储列表中
    html = get_page(url_of_illness)
    get_doctor_url_list(html)
    print(len(url_all_doctors))

    # 查看一共多少页,存储在number_of_pages中
    number_of_pages = get_pages_number(html)

    # 检查网页的结构化，防止html和htm不一致造成的影响。
    n = check_page_structure(url_of_illness)

    # 开始offset迭代
    for i in range(2, number_of_pages + 1):
        main(offset=i, n=n)

    # 写入文件
    write_csv(csv_file_name, url_all_doctors, illness_name)