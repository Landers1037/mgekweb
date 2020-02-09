# simple-site

一个使用Bootstrap模板的简单flask网站

#### 环境python3.7

```python
Flask==1.0.3
Jinja2==2.10.1
Werkzeug==0.15.4
```

#### 示例

![demo1](/store/simple-site/demo2.png)

![demo2](/store/simple-site/demo1.png)

#### 使用

使用`git clone https://github.com/Landers1037/flasksite.git`克隆本示例

直接测试环境

```shell
python3 app.py
```

使用gunicorn代理

**需要自行安装gunicorn**

```python
pip3 install gunicorn
```

使用gunicorn代理flask应用

```shell
cd flasksite
gunicorn -w 2 -b 127.0.0.1:5000 app:app --reload
```

