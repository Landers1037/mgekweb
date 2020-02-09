from flask import Flask
from flask import redirect,render_template,url_for,jsonify,send_from_directory
from static.database import data
from flask_restful import Api,Resource
from datetime import date
from xhj import xhj
import os,datetime,json
from requests import get
from flask_sqlalchemy import SQLAlchemy
import click


app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'mgek.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 关闭对模型修改的监控
app.jinja_env.auto_reload = True
# app.debug = True
api = Api(app)
db = SQLAlchemy(app)

@app.route('/')
def main():
    apps = data["apps"]
    return render_template('index.html',apps=apps)

# 移动端优化
@app.route('/mobile/')
def main_mobile():
    apps = data["apps"]
    return render_template('index_m.html',apps=apps)

@app.route('/landers')
def main_landers():
    apps = data["apps"]
    return render_template('landers.html',apps=apps)

# 关于
@app.route('/about/')
def about():

    return render_template('about.html')
# gallery
@app.route('/gallery/')
def gallery():
    list = [
        'http://img.mgek.cc/images/43f44188bf.jpg',
    'http://img.mgek.cc/images/d0a083c854.jpg',
    'http://img.mgek.cc/images/68f6de018b.jpg',
    'http://img.mgek.cc/images/1b20c3c8e1.jpg',
    'http://img.mgek.cc/images/3eb0aafb78.jpg',
    'http://img.mgek.cc/images/1fdca5fdaa.jpg',
    'http://img.mgek.cc/images/79a218132a.jpg',
    'http://img.mgek.cc/images/985bb24adb.jpg',
    'http://img.mgek.cc/images/bc636ad7cf.jpg',
    'http://img.mgek.cc/images/51d2079d67.jpg',
    'http://img.mgek.cc/images/4176ae9e23.jpg',
    'http://img.mgek.cc/images/782ec99183.jpg',
    'http://img.mgek.cc/images/03fab094d3.jpg',
    'http://img.mgek.cc/images/903c9eef2d.jpg',
    'http://img.mgek.cc/images/352dc76c90.jpg',
    'http://img.mgek.cc/images/df05fdb998.jpg',
  ]
    return render_template('gallery.html',list=list)

# app详情页
@app.route('/app/<string:name>/')
def app_choose(name):

    return send_from_directory(os.getcwd()+'/static/app/',name+'.html')

@app.route('/app/color-picker/')
def app_color():

    color = data["color"]
    return render_template('color-picker.html',color=color)

# IP地址池爬虫
@app.route('/app/crawler/')
def crawler():
    data1 = ip_xici.query.filter_by(title="匿名代理").all()
    data2 = ip_xici.query.filter_by(title="透明代理").all()
    data3 = ip_xici.query.filter_by(title="https代理").all()
    data4 = ip_xici.query.filter_by(title="http代理").all()
    return render_template('crawler.html',data1=data1,data2=data2,data3=data3,data4=data4)

# 帮助文档
@app.route('/doc/')
def doc_index():
    docs = data["docs"]

    return render_template('doc_index.html',docs=docs)

@app.route('/<string:name>.md')
def doc(name):

    return render_template('doc.html',name=name)

@app.route('/doc.about/')
def doc_about():
    name = "about"
    return render_template('doc.html',name=name)

# gitbook在线

@app.route('/book/<string:name>/')
def book_go(name):

    return app.send_static_file('book/'+name+'/index.html')

@app.route('/book/suanfa/ch<string:num>/')
def book_ch(num):

    return app.send_static_file('book/suanfa/ch'+num+'/index.html')

# 公共库
@app.route('/public/')
def public():
    list = data["pub"]
    return render_template('public.html',list=list)

@app.route('/public/<string:name>')
def public_detail(name):

    return app.send_static_file('public/'+name+'.html')

@app.route('/public/ip-trackers')
def public_ip():
    now = datetime.date.today()
    data1 = get('https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt').text
    data2 = get('https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt').text
    return render_template('ip-trackers.html',data1=data1,data2=data2,time=now)

@app.route('/public/block-ad')
def public_ad():

    return app.send_static_file('public/block-ad.html')

@app.route('/public/block-ad/<string:name>')
def public_ad_name(name):

    data = get('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/'+name).text
    return render_template('block-ad.html',data=data)

# 站点地图
@app.route('/sitemap.xml')
def sitemap():

    return app.send_static_file('sitemap.xml')

#使用
@app.route('/usage/')
def usage():

    return render_template('usage.html')

# api接口
@app.route('/api/')
def _api():
    datenow = date.today()
    return render_template('api.html',date=datenow)

class Getstate(Resource):
    def get(self,date):
        return jsonify(data)

class Getssr(Resource):
    def get(self,date):
        # return xhj()
        ssrapi = get('http://api.mgek.cc/ssr').text
        return ssrapi

class Gethtml(Resource):
    def get(self):
        list1 = os.listdir('templates')
        list2 = os.listdir('static')
        list3 = os.listdir('static/css')
        list4 = os.listdir("static/js")
        list5 = os.listdir('static/docs')
        return jsonify("templates",list1,"static",list2,"css",list3,"js",list4,"docs",list5)

class Getip(Resource):
    def get(self,date):
        from all import iplist
        return jsonify(iplist)

api.add_resource(Getstate,'/api_v1/<string:date>/')
api.add_resource(Getssr,'/api_v2/<string:date>/')
api.add_resource(Gethtml,'/api_v3/')
api.add_resource(Getip,'/api_v4/<string:date>/')

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('error.html')

@app.errorhandler(500)  # 传入要处理的错误代码
def page_error(e):  # 接受异常对象作为参数
    return render_template('error.html')

class ip_xici(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 标题
    ip = db.Column(db.String(255))  # ip
    port = db.Column(db.String(20))


@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.cli.command()
def sub():
    db.create_all()
    from all import iplist
    # 全局的两个变量移动到这个函数
    for ip in iplist[0]:
        ips = ip_xici(title='匿名代理',ip=ip["ip"],port=ip["port"])
        db.session.add(ips)

        db.session.commit()
    for ip in iplist[1]:
        ips = ip_xici(title='透明代理',ip=ip["ip"],port=ip["port"])
        db.session.add(ips)

        db.session.commit()
    for ip in iplist[2]:
        ips = ip_xici(title='https代理',ip=ip["ip"],port=ip["port"])
        db.session.add(ips)

        db.session.commit()
    for ip in iplist[3]:
        ips = ip_xici(title='http代理',ip=ip["ip"],port=ip["port"])
        db.session.add(ips)

        db.session.commit()
    click.echo('Done.')



if __name__ == '__main__':
    app.run()