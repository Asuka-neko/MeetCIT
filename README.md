# MeetCIT
 
打工指南：装python3 装django 看一遍django doc（可选）

怎么润：
0. 因为现在database可能同步了我的，为了防止bug，下下来以后换branch，然后把`MeetCIT/db.sqlite3`删了，`MeetCIT/cal/migration`和`MeetCIT/users/migration`里面除了`__init__.py`的别的东西都删掉；任何的terminal提示migration相关warning和报错都可以这么解决
1. `cd`到有manage.py的文件夹，`python3 manage.py makemigrations`
2. `python3 manage.py migrate`
3. `python3 manage.py runserver` migrate过一次以后只run这个就行

现在有的页面们：
1. http://localhost:8000/homepage 首页
2. http://localhost:8000/accounts/login/ login
3. http://localhost:8000/accounts/password_change/ 换密码
4. http://localhost:8000/accounts/password_change/done/ 成功换密码
5. http://localhost:8000/register/ 注册
6. http://localhost:8000/calendar/ 日历首页

任务列表：
1. book按钮
2. unbook按钮
3. 个人profile页面
4. 一些朴素直男页面需要小设计师把它弄好看；style相关在`./users/templates/里面
  :> LSF 接了这个任务了
5. 酷炫logo（优先度低）
