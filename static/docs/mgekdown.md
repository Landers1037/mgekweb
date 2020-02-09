# mgekdown
a markdown to html tool using in flask

如果之前使用hexo等静态博客生成工具，现在想将文章转移到flask站点

不需要将原来的`.md`文件输出到数据库，只需要使用本工具直接渲染`.md`文件为html

### 测试环境

```python
flask==1.0.3
```

### 需求

原本的hexo引擎模板应该如下

```markdown
---
title: {{ title }}
date: {{ date }}
tags:
categories:
abstract:

---

正文摘要

<!--more-->
```

```html
<!--more-->标签用于判断文章摘要
```

安装需要的库

```python
pip3 install markdown
```

### 使用

#### 在flask中引入mgekdown.py

```python
from markdown import markdown
from mgekdown import Mgekdown as mgd
```

#### 添加flask的Jinjia过滤器

```python
@app.template_filter('md')
def markdown_to_html(txt):
    return markdown(txt)
```

#### 添加博客文章路由

```python
@app.route('/blog/post/<string:name>/')
def blog_post(name):
    txt = mgd.read('post/'+ name.replace('/','')+'.md')
    content = mgd.content(txt)
    title = mgd.title(txt)

    return render_template('blog_post.html',content=content,title=title)
```

#### html模板

```html
{% extends 'base.html' %}
{% block title %}博客{% endblock title %}   
<div class="list-group">
        <div class="list-group-item">
            {{ post|md|safe}}
        </div>
    </div>
{% endblock body %}
```

使用`{{ post|md|safe}}`自定义的md过滤器渲染markdown文本内容

### 示例

md文件

```markdown
---
title: 微信公众号同步推出
tags:
  - 建站
url: 572.html
id: 572
categories:
  - 随笔
date: 2018-04-17 13:13:47
---

扫码关注 你的关注就是我的动力<!--more-->

因为懒公众号停运
```

去掉顶部标签获取正文

```python
txt = m.read('post/weixinqrcode.md')
print(m.content(txt))
>>>
扫码关注 你的关注就是我的动力<!--more-->

因为懒公众号停运
```

获取标题

```python
txt = m.read('post/weixinqrcode.md')
print(m.title(txt))
>>>
微信公众号同步推出
```

获取文章摘要

```python
txt = m.read('post/weixinqrcode.md')
print(m.abstract(txt))
>>>
扫码关注 你的关注就是我的动力
```

#### 接口

```python
mgd = Mgekdown()
```

`mgd.filelist(path)` 读取存放md文件的目录返回文件名称列表，名称经过url规范编码处理可以直接加入flask路由

`mgd.read(file)` 读取md文件的内容

`mgd.content(txt)` 对md格式文本处理，提取正文内容

`mgd.title(txt)` 对md格式文本处理，提取标题

`mgd.date(txt)` 对md格式文本处理，提取时间(默认只提取年月日)

`mgd.abstract(txt)` 对md格式文本处理，获取文章摘要

#### 扩展

预处理的markdown格式对`pre`,`code`,`br`标签支持不好

添加markdown的扩展参数

```python
markdown(txt,extensions=['markdown.extensions.fenced_code','markdown.extensions.extra','markdown.extensions.smarty','markdown.extensions.nl2br'])
```

