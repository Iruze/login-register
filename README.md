## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP
## 该项目教程发布在www.django-test.com

## 简单的使用方法：


创建虚拟环境
- 使用`pip`安装第三方依赖, `pip3 install -r requirements.txt`
- 修改`settings.example.py`文件为`settings.py`, 并配置相关信息
- 运行`migrate`命令，创建数据库和数据表       
  ```shell
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
- 运行`python3 manage.py runserver 127.0.0.1:4444`启动服务器


路由设置：

```python
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]   
```