#/usr/bin/env python
#-*-coding:utf-8-*-
import tornado.web

LIST_INFO=[
    {"username":"aa","email":"pyrene3110436742@162.com"}
]
for i in range(99):
    temp={"username":"bb"+str(i),"email":str(i)+"123"}
    LIST_INFO.append(temp)

class Pagination:
    #下面封装的参数分别为，当前页数，和总的数据
    def __init__(self,current_page,all_item):   #初始化当前页和总页数
        all_pager,c=divmod(all_item,5)   #all_pager为计算的到的总页数，要经过下面的判断
        if c>0:
            all_pager+=1
        self.all_pager=all_pager

        try:                                    #为当前页处理异常
            current_page=int(current_page)
        except Exception:
            current_page=1
        if current_page<1:
            current_page=1
        self.current_page=current_page


    # 加上这样的装饰器，会使下面调用这个方法的时候以访问字段的形式来访问，也就是不用加上括号
    @property
    def start(self):                        #当前页的起始数据
        return (self.current_page-1)*5
    @property
    def end(self):                          #当前页的结尾数据
        return self.current_page*5

    def page_str(self,base_url):            # 生成页码逻辑
        list_page=[]
        if self.all_pager<11:
            s=1
            t=self.all_pager
        else:
            if self.current_page<=6:
                s=1
                t=11
            else:
                if( self.current_page+5)>self.all_pager:
                    s=self. current_page-10
                    t=self. current_page
                else:
                    s= self.current_page-5
                    t= self.current_page+5
        #首页
        first_page='<a  href="%s1">首页</a>'%(base_url,)
        list_page.append(first_page)

        #上一页 current_page-1 在javascript中加上javascript:void(0)表示什么也不做
        if self.current_page==1:
            pre_page='<a href="javascript:void(0)">上一页</a>'
        else:
            pre_page='<a  href="%s%s">上一页</a>'%(base_url,self.current_page-1)
        list_page.append(pre_page)

            #中间页数
        for p in range(s,t+1):
            if p == self.current_page:
                temp='<a class="active" href="%s%s">%s</a>' %(base_url,p,p) #这里设置自定义url
            else:
                temp='<a class-"active" href="%s%s">%s</a>'%(base_url,p,p)
            list_page.append(temp)
        #尾页
        last_page='<a  href=%s%s>尾页</a>'%(base_url,self.all_pager)
        list_page.append(last_page)

        #下一页 current_page+1 在javascript中加上javascript:void(0)表示什么也不做
        if self.current_page>=self.all_pager:
            next_page='<a href="javascript:void(0)">下一页</a>'
        else:
            next_page='<a  href="%s%s">下一页</a>'%(base_url,self.current_page+1)
        list_page.append(next_page)

        #跳转页面
        jump='''<input type="text" /><a  onclick="jump('%s',this);">GO</a>'''%(base_url,)
        script='''<script>
        function jump(baseUrl,ths){
            var val=ths.previousElementSibling.value;
            if(val.trim().length>0){
                location.href=baseUrl+val
            }
        }
        </script>'''
        list_page.append(jump)
        list_page.append(script)
        return "".join(list_page)                       #直接返回值


class IndexHandler(tornado.web.RequestHandler):
    def get(self,page):

        page_obj=Pagination(page,len(LIST_INFO))                    #传入当前页和总页数生成对象
        current_list=LIST_INFO[page_obj.start:page_obj.end]        #以字段的方式来应用类中的方法
        str_page=page_obj.page_str("/index/")                       #传入自己自定义的url

        # 传入参数，当前页的参数和页码数的参数
        self.render("home/index.html" ,list_info=current_list,current_page=page_obj.current_page,str_page=str_page)


    def post(self,page):
        user=self.get_argument("username")
        email=self.get_argument("email")
        temp={"username":user,"email":email}
        LIST_INFO.append(temp)
        self.redirect("/index/"+page)
