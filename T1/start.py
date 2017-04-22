#/bin/usr/env python
#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from controllers import home
from settings import Setting
from controllers import extend

#路由映射，路由系统
application=tornado.web.Application(
    [(r"/index/(?P<page>\d*)",home.IndexHandler),
     # (r"/index",extend.IndexHandler),
     (r"/ff",extend.FFHandler)
     ],
    **Setting.settings
)
# application.add_handlers("www.cnblogs.com",[
#     (r"/index/(?P<page>\d*)",)
# ])

if __name__=="__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
