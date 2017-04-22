#/usr/bin/env python
#-*-coding:utf-8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("extend/index.html",List_info=[11,12,13])
class FFHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("extend/ff.html",List_info=[11,12,13])