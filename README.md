# BlogSite
##develop environment

    python3.4.2
    django1.7
    jieba
    pytz
    
    
###jieba安裝方法

    git clone https://github.com/fxsjy/jieba.git
    python3 setup.py install

###pytz安裝方法

    sudo pip3 install pytz
    
###功能
- 书写博客（标题，内容）
- 按照内容自动获得标签，分类，时间。
- 在右侧可以按照标签，分类，时间，点击数作为归档类型，查找相应的文章
- 文章，归类的URL在每次生成以及修改后URL会随机变换为一串“数字+字母”的字符串
- 具有简单的搜索功能

###写它的原因
希望通过这个博客程序练习python+django+bootstrap写网站的方法
