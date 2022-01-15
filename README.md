# MeetCIT
 
打工指南：装python3 装django 看一遍django doc（可选）

怎么润：
0. 因为现在database可能同步了我的，为了防止bug，下下来以后换branch，然后把`MeetCIT/db.sqlite3`删了，`MeetCIT/cal/migration`和`MeetCIT/users/migration`里面除了`__init__.py`的别的东西都删掉；任何的terminal提示migration相关warning和报错都可以这么解决
1. `cd`到有manage.py的文件夹，`python3 manage.py makemigrations`
2. `python3 manage.py migrate`
3. `python3 manage.py runserver` migrate过一次以后只run这个就行

现在有的页面：
1. http://localhost:8000/homepage 首页
2. http://localhost:8000/dashboard/ dashboard 可以login logout register 换密码
4. http://localhost:8000/accounts/login/ login
5. http://localhost:8000/accounts/password_change/ 换密码
6. http://localhost:8000/accounts/password_change/done/ 成功换密码
7. http://localhost:8000/register/ 注册
8. 一些邮件send reset link相关页面

任务列表：
1. 开任务之前给自己建一个branch
2. 一些朴素直男页面需要小设计师把它弄好看；style相关在`./users/templates/里面
  :> LSF 接了这个任务了
3. 酷炫logo（优先度低）
