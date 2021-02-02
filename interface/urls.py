# @Author: Administrator
# @Email: 2478711969@qq.com
# @Date: 2021/2/2 15:27
# @File: urls
# @Project: SimpleInterface
# @Desc:
from django.urls import path
from interface.views import CustomAuthToken

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
]

