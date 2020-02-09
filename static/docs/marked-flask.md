# Marked-Flask

marked-flask是一个基于marked.js实现的flask直接md文件渲染html页面框架

使用flask后端传入需要渲染的`.md`文件，前端使用marked.js渲染为html页面

默认使用`github-markdown-css`提供的页面样式

使用`atom-one-light.min.css`代码高亮样式

使用`highlight.js`作为代码块渲染工具

使用Ajax异步获取本地md文件局部刷新页面

### 使用

```bash
$ git clone https://github.com/Landers1037/marked-flask.git
```

安装依赖

```python
pip3 install -r requirements.txt
```

启动

```python
python3 app.py
```

### 示例

![demo1](http://file.mgek.cc/images/mgek/marked-flask/demo1.png)

![demo2](http://file.mgek.cc/images/mgek/marked-flask/demo2.png)

[测试内容](/demo.md)

### 参数

后台使用flask的`render_template('post.html',name=name)`传入参数name作为获取的md文件名称

`doc.js`会自动在`/docs/`目录下寻找`*.md`文件并渲染

### 进阶使用

使用数据库存储后台`md`文件名称索引

在flask渲染模板中传入数据库中的文章字符串即可实现全部文章的即时渲染