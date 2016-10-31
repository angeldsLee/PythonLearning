# -*- coding: UTF-8 -*-

import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
# 这里只定义了一组匹配，那就是 '/', 'index' 的匹配。它的含义是：
# 如果有人使用浏览器访问 / 这一级目录，lpthw.web
# 将找到并加载 class index，从而用它处理这个浏览器请求

render = web.template.render('templates/')


# 告诉lpthw.web 到哪里去找到模板进行加载，以及如何渲染(render)这个模板


class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting=greeting)  # 渲染
    """
    render 调用的函数名称只要跟 templates/下的 .html 文件名匹配到，这个 HTML 模板就可以被渲染到了
    """


"""
在bin/app.py里面添加了一个叫做render的新变量，它本身是一个 web.template.render对象。
将templates/ 作为参数传递给了这个对象，让render 知道了从哪里去加载模板文件。
在后面的代码中，当浏览器一如既往地触发了index.GET 以后，它没有再返回简单的greeting字符串，取而代之的是
调用了 render.index，而且将问候语句作为一个变量传递给它。
这个render_template函数可以说是一个“魔法函数”，它看到了需要的是index.html，
于是就跑到templates/目录下，找到名字为index.html 的文件，然后就把它渲染(render)一遍（叫“转换一遍”也可以）。
在templates/index.html文件中，看到初始定义一行中说这个模板需要使用一个叫greeting的参数，这和函数定义中的格式差不多。
另外和 Python 语法一样，模板文件是缩进敏感的，所以要确认自己弄对了缩进。
最后，你让templates/index.html去检查greeting这个变量，如果这个变量存在的话，就打印出变量的内容，
如果不存在的话，就会打印出一个默认的问候信息。
"""
if __name__ == "__main__":
    app.run()
