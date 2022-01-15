# MeetCIT
 
打工指南：装python3 装django 看一遍django doc（可选）

怎么润：
1. `cd`到有manage.py的文件夹，`python3 manage.py makemigrations`
2. `python3 manage.py migrate`
3. `python3 manage.py runserver` migrate过一次以后只run这个就行

现在有的页面：
1. http://localhost:8000/dashboard/ dashboard 可以login logout register 换密码
2. http://localhost:8000/accounts/login/ login
3. http://localhost:8000/accounts/password_change/ 换密码
4. http://localhost:8000/accounts/password_change/done/ 成功换密码
5. http://localhost:8000/accounts/register/ 注册

任务列表：
1. 开任务之前给自己建一个branch
2. 一些朴素直男页面需要小设计师把它弄好看；style相关在`./users/templates/里面
3. 酷炫logo（优先度低）
