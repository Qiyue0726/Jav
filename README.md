### 这是我学习 Python 爬虫和 Django 做的一个小项目，可以实时爬取 Javlib 的优优最新作品，数据库内已经爬取了截止至 2021-05-29 的所有优优信息，可以直接搜索并加入列表，通过点击 关注列表 可以添加关注。也可以在管理界面进行操作



---



### 安装必备模块

```shell
pip install beautifulsoup4 requests lxml Django django-cors-headers django-rest-framework
```



### 启动项目

```shell
python manage.py runserver 0.0.0.0:8080
```



* [首页](http://localhost:8000)
* [后台管理](http://localhost:8000/admin)   **账户：** admin  **密码：** 333

![image](https://user-images.githubusercontent.com/33934935/120342755-aa694300-c32a-11eb-92f7-22e2f2ffba42.png)

![image](https://user-images.githubusercontent.com/33934935/120343071-f9af7380-c32a-11eb-95a4-6a0dc7cf658a.png)
