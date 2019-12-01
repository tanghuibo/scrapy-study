# pyhton爬虫框架scrapy学习

## scrapy

### 安装

```bash
pip3 install scrap
```

scrapy命令简介

| 名称         | 说明                                                         | 例子                                                |
| ------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| help         | 用于查看帮助信息                                             | scrapy -help                                        |
| version      | 查看版本信息，可见-v参数查看各组件的版本信息                 | scrapy version –v                                   |
| startproject | 用于创建一个工程，并创建一个完整的工程目录                   | scrapy startproject name                            |
| genspider    | 在工程中产生一个spider，可产生多个spider，不同的spider要求name不同 | scrapy genspider name(爬虫名) kgc.com（爬取的域名） |
| list         | 查看本工程中有哪些spider（爬虫）                             | scrapy list                                         |
| view         | 查看你所或得的页面源码在浏览器中显示的样子                   | scrapy view                                         |
| parse        | 判断我们写的parse是否有正确                                  | scrapy parse http://kgc.cn/                         |
| shell        | 进入python的交互式环境中                                     | scrapy shell                                        |
| runspider    | 运行自包含的爬虫                                             | scrapy runspiderspider.py(爬虫文件)                 |
| bench        | 执行一个基准的测试，用来检测Scrapy是否安装成功               | scrapy bench                                        |
| crawl        | 运行一个爬虫                                             | scrapy crawl zhipin                                        |


### 快速开始

#### 1. 创建爬虫工程

```bash
scrapy startproject scrapy_study
```
通过该命令创建出如下文件列表:

```text
├── scrapy.cfg
└── scrapy_study
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── __pycache__
    ├── settings.py
    └── spiders
        └── __init__.py
```

### 2. 创建爬虫

```bash
scrapy genspider zhipin www.zhipin.com
```

### 3. 在items中编写爬取文件的数据结构

```python
class ZhipinScrapyItem(scrapy.Item):
    # 职务
    job = scrapy.Field()
    # 薪酬
    money = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    pass
```

### 4. 屏蔽 robots协议检查(仅限于学习)

爬虫框架在网站中查询robots协议，判断网站是否可爬取。

修改 settings.py

```python
ROBOTSTXT_OBEY = False
```

### 5. 修改user-agent

user-agent包含客户端信息，爬虫框架默认的agent一般会被服务器直接拒绝

```python
# 设置用户代理池
MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

# agent
USER_AGENT = random.choice(MY_USER_AGENT)
```

### 6. 编写爬虫主代码

```python
# -*- coding: utf-8 -*-
import scrapy

from scrapy_study.items import ZhipinScrapyItem
from scrapy_study.uitls.csvMaker import CsvMaker


class ZhipinSpider(scrapy.Spider):

    scvMaker = CsvMaker("result.csv", ['job', 'money', 'desc', 'url'])
    name = "zhipin"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/gongsir/5d627415a46b4a750nJ9_100000.html?page=1&ka=page-1"]

    def parse(self, response):
        job_list = response.xpath("//div[@class='job-list']/ul/li")
        for job in job_list:
            item = ZhipinScrapyItem()
            item['job'] = job.xpath(".//div[@class='job-title']/text()").extract_first()
            item['money'] = job.xpath(".//div[@class='title-box']/span[@class='red']/text()").extract_first()
            item['desc'] = job.xpath(".//div[@class='job-primary']/div[@class='info-primary']/p/text()").extract_first()
            item['url'] = job.xpath(".//a/@href").extract_first()
            self.scvMaker.add(item)
        next = response.xpath("//div[@class='page']/a[@class='next']/@href").extract()
        if next:
            yield scrapy.Request("https://www.zhipin.com" + next[0], callback=self.parse)
        pass
```

####

#### 7. 设置cookie
通过 `middlewares.py` 修改cookie

middlewares.py:
```python
class ScrapyStudyDownloaderMiddleware(object):
    def __init__(self):
        with open("cookie.txt", "r") as f:
            self.cookie_text = f.read()
            print("cookie:" + self.cookie_text)

    def process_request(self, request, spider):
        request.headers["cookie"] = self.cookie_text
```
cookie从 `cookie.txt`中读取，目前需要用户手动输入

修改`settings.py`

settings.py:
```python
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
   'scrapy_study.middlewares.ScrapyStudyDownloaderMiddleware': 543,
}
```

#### 运行爬虫

```bash
scrapy crawl zhipin
```
运行结果见: `result.csv`

### 现存问题

网站的cookie是动态生成的，相同cookie只能发送5~6条请求
