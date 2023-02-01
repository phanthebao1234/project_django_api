# CÁC BƯỚC TẠO API

1. Bước 1:
- Tạo môi trường chạy dự án: py -m venv .venv
- Chạy môi trường ảo với shell: .venv\Scripts\Activate.ps1
- Khởi tạo dự án: django-admin startproject django_project

2. Bước 2:
- Tạo 1 app với tên là todos: py manage.py startapp todos
- Vào setting.py trong thư mục root(django_project), trong phần INSTALLED_APPS ta thêm đăng kí app tên là 'todos'
- Tiếp tục là vào urls.py của thư mục root tạo đường dẫn sau path admin: 
    path('api/', include(urls.todos))
    
3. Bước 3:
- Tạo 1 đối tương todos trong thư mục model Todos
- Sau đó chạy câu lệnh để tạo dbs: 
   ` py manage.py makemigrations todos`
    `py manage.py migrate`

4. Bước 4:
- Trong todos/admin.py ta đăng kí cho đối tường todos vào trang quản trị
- Sau đó ta thêm 1 lớp TodoAdmin để hiển thị
    
5. Bước 5:
- Tạo 1 tài khoản để đăng nhập vào trang quản trị:
    py manage.py createsuperuser
    username: phthebao
    email: phthebao@gmail.com   
    password: 123
- Tạo 3 cột dữ liệu trong bảng Todos

6. Bước 6: 
- Cài đặt thư viện Rest framework django
    python -m pip install djangorestframework~=3.13.0
- Đăng kí sử dụng trong INSTALLED_APPS
    'rest_framework'
- Thêm 1 dòng tại vị trí cuối tệp để sử dụng AllowAny 
    REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES":
        [
            "rest_framework.permissions.AllowAny",
        ],
    }

7. Bước 7: 
- Trong todos/urls.py: Tạo 2 đường dẫn là ListTodo và DetailTodo
    
8. Bước 8:
- Trong thư mục todos, tạo serializer.py để chuyển đổi mô hình(model) thành kiểu dữ liệu dạng JSON.
    
9. Bước 9:
- Trong todos/views.py, tạo 2 lớp đối tượng như trong urls là ListTodo và DetailTodo
    
# BẢO MẬT CROS
### -Thiết lập ở 3 vị trí sau: 
*   Thêm phần corsheaders vào INSTALLED_APPS
*   Thêm CorsMiddleware phía trên CommonMiddleWare trong MIDDLEWARE
*   Tạo cấu hình CORS_ALLOWED_ORIGINS ở cuối tệp

# DELOY API BACKEND
* Định lại các tệp tĩnh với Whitenoise
* Cài đặt Gunicorn làm máy chủ web
* Tạo các tệp tests.txt, runtime.txt và Procfile
* Cập nhật cấu hình ALLOWED_HOSTS

    - `mkdir static`
    - `python -m pip install whitenoise`
#### WhiteNoise phải được thêm vào django_project/settings.py ở các vị trí sau:
* Whitenoise phía trên django.contrib.staticfiles trong INSTALLED_APPS
* WhiteNoiseMiddleware phía trên CommonMiddleware
* Cấu hình STATICFILES_STORAGE trỏ tới WhiteNoise
- Cuối cùng chạy lệnh `python manage.py collectstatic`

*Gunicorn sẽ được sử dụng làm máy chủ web sản xuất và có thể được cài đặt trực tiếp.*
`python -m pip install gunicorn`
- Với trình soạn thảo văn bản của bạn, hãy tạo tệp runtime.txt trong thư mục gốc của dự án bên cạnh manage.py. 
    `python-3.10.2`
Nó sẽ có một dòng chỉ định phiên bản Python để chạy trên Heroku.
- Tiếp tục tạo file Procfile.txt với nội dung:
    `web: gunicorn django_project.wsgi --log-file -`
- Tiếp tục ta có thể tạo tự động tệp tests.txt bằng cách:
    `python -m pip freeze > tests.txt`
- Bước cuối cùng là cập nhật cấu hình ALLOWED_HOSTS trong django_project/settings.py.
- Quyền truy cập phải được giới hạn đối với máy chủ cục bộ, 127.0.0.1 và .herokuapp.com.
- Trong django_project/settings.py ta cấu hình:
`ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]`
