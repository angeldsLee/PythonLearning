# -*- coding: UTF-8 -*-

import web

urls = (
    '/hello', 'Index1'
)

app1 = web.application(urls, globals())
# 这里只定义了一组匹配，那就是 '/', 'index' 的匹配。它的含义是：
# 如果有人使用浏览器访问 / 这一级目录，lpthw.web
# 将找到并加载 class index，从而用它处理这个浏览器请求

render = web.template.render('templates/')


# 告诉lpthw.web 到哪里去找到模板进行加载，以及如何渲染(render)这个模板


class Index1(object):
    def GET(self):
        form = web.input(name="nobody")
        greeting = "hello, %s" % form.name
        return render.index1(greeting=greeting)  # 渲染

    """
    render 调用的函数名称只要跟 templates/下的 .html 文件名匹配到，这个 HTML 模板就可以被渲染到了
    """


"""

"""
if __name__ == "__main__":
    app1.run()
