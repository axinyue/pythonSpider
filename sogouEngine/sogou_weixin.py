import requests



'''
http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%BB%95%E5%9F%8E%E7%9D%80%E7%81%AB&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=2058&sst0=1534131351137&lkt=0%2C0%2C0
http://weixin.sogou.com/weixin?query=%E7%BB%95%E5%9F%8E%E7%9D%80%E7%81%AB&_sug_type_=&sut=2058&lkt=0%2C0%2C0&s_from=input&_sug_=y&type=2&sst0=1534131351137&page=2&ie=utf8&w=01019900&dr=1
'''
'''
"weixin":"http://weixin.sogou.com/weixin", #p=42341200&query=绕城着火&type=2&ie=utf8
"web":"http://www.sogou.com/web",# ?ie=utf8&query=%E7%BB%95%E5%9F%8E%E7%9D%80%E7%81%AB"
"news":"http://news.sogou.com/news?" #http://news.sogou.com/news?ie=utf8&p=40230447&interV=kKIOkrELjboJmLkElbYTkKIKmbELjbkRmLkElbkTkKIRmLkEk78TkKILkY==_-399983173&query=%E7%BB%95%E5%9F%8E%E7%9D%80%E7%81%AB&
        
'''

class SogouSearchEngine(object):
    def __init__(self):
        self.category = {
           "weixin":"http://weixin.sogou.com/weixin", #p=42341200&query=绕城着火&type=2&ie=utf8
            "web":"http://www.sogou.com/web",# ?ie=utf8&query=%E7%BB%95%E5%9F%8E%E7%9D%80%E7%81%AB"
        }
        pass
    def request(self,url,parms,**kwargs):
        return requests.get(url,parms,**kwargs)

    def weixin_get(self,query="",type="2",ie="utf8",get_page=None):
        '''
        :param query: 关键词
        :param type:
        :param ie:
        :parm get_page:需要获取几页.如果get_page>总页数,将获取全部.get_page<总页数,获取<=get_page页.
        :return:
        '''
        url = self.category.get("weixin")
        parms ={"query":query,"type":type,ie:ie}
        r = self.request(url,parms)

        #TODO 数据&url,匹配获取.入库.多页获取
        self.write(r,"weixin_text.html")
    def write(self,request,file):
        with open(file, "wb") as f:
            f.write(request.content)

    def categoryFileter(self):
        # 多种类型(新闻,微信,网页..)去重
        pass

if __name__ == "__main__":
    SogouSearchEngine().weixin_get("绕城着火")
    pass
