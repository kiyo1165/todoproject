from django.contrib import admin
from django.urls import path, include # includeメソッドの呼び出し

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')), # pathが''の場合はルートディレクトリにデフォルトで設定になる。
]