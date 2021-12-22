import os
from django.core.mail import send_mail


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自zzw的测试邮件',
        '欢迎访问www.zzw.com， 这里是张子文的博客和教程站点，本站专注于python， django和机器学习技术的分享.',
        'zhangziwen005@sina.com',
        [''],
    )
