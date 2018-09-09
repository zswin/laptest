from lxml import etree

my_page = '''<html>
        <title>TITLE</title>
        <body>
        <h1>我的博客</h1>
        <div>我的文章</div>
        <div id="photos">
         <img src="pic1.jpeg"/><span id="pic1">PIC1 is beautiful!</span>
         <img src="pic2.jpeg"/><span id="pic2">PIC2 is beautiful!</span>
         <p><a href="http://www.example.com/more_pic.html">更多美图</a></p>
         <a href="http://www.baidu.com">去往百度</a>
         <a href="http://www.163.com">去往网易</a>
         <a href="http://www.sohu.com">去往搜狐</a>
         wtf
        </div>
        <p class="myclassname">Hello,\nworld!<br/>-- by Adam</p>
        <div class="foot">放在尾部的其他一些说明</div>
        </body>
        </html>'''

html = etree.fromstring(my_page)
txt1 = html.xpath('//div/text()')
#txt2 = html.xpath('//div[@id="photos"]/a[3]/text()')
txt2 = html.xpath('//div[@id]/text()')
txt3 = html.xpath('//div[@class="foot"]/text()')[0]
txt4 = html.xpath('//div[@*]/text()')#有属性的div
txt5 = html.xpath('//div[1]/text()')
txt6 = html.xpath('//div[last()-1]/text()')
txt7 = html.xpath('//div[position() < 2]/text()')
txt8 = html.xpath('//div/text() | //h1/text()')

val1 = html.xpath('//div/a/@href')
val2 = html.xpath('//div/img/@src')
val3 = html.xpath('//div/span[@id]/text()')
val4 = html.xpath('//div/span/@id')
val5 = html.xpath('//div[2]/@id')

tst1 = html.xpath('//div[position()<3]/a/@href')
print(tst1)
tst2 = html.xpath('//div[position()<3]//a/@href')
print(tst2)
