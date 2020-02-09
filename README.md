# mgekweb
demo of my web site

### 这是我的站点demo源码

你可以在这里访问站点[http://mgek.cc](http://mgek.cc)

### 介绍

使用Flask轻量框架开发的web站点，用于展示我的个人项目

前端使用flask的jinja2模板语言开发

这里是一个使用**vue**开发的站点[code.mgek.cc](http://code.mgek.cc)

站点包括了

1. 个人项目展示
2. doc文档预览（使用marked.js实现的即时渲染
3. 网络爬虫页面，用于定时爬取站点展示的公共资源
4. 一个图床demo页面，图床后台使用nginx的缓存加速



### 部署

使用Nginx+gunicorn的方式部署于linux主机

#### Docker化

站点同时支持使用docker构建微服务