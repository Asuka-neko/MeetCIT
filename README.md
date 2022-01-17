# MeetCIT

玩耍指南
1. 装Python 3
2. 装django
3. 在GitHub Desktop里把main pull下来
4. 打开terminal，安装下面两个包
5. pip install django-bootstrap4
6. pip install django-guardian
7. 然后cd到github那个有manage.py的文件夹
8. python3 manage.py makemigrations
9. python3 manage.py migrate
10. python3 manage.py runserver
11. http://localhost:8000/homepage
12. 打开首页进去玩

任务列表：
1. 一些朴素直男页面需要小设计师把它弄好看；style相关在`./users/templates/里面
  :> LSF 接了这个任务了
2. 酷炫logo（优先度低）




TEAM MEMBERS: 
Donglun He, Wenyi Huang, Yao Jiang, Shufan Liu, Mingxin Xue

PROJECT NAME: 
MeetCIT

PROJECT OBJECTIVE: 
We plan to design an appointment reservation website for MCIT students. The 
reasons for the meeting are not limited to mentor/mentee, but can also include 
students who don’t know each other but want to broaden their networks. 

PROJECT DESCRIPTION: 
- Users will need to sign up and to choose their roles as either mentor or mentee. 
Users will login to use the website. 
- Mentors will need to edit their personal profile: Name, year, specialized field, 
and free time slot during the week. 
- Once logged in, mentees will have the page with all available time slots shown, 
hosted by different mentors. 
- Mentees can select any available time slots they desire. Mentees can click on one 
slot and view the selected mentor’s profile. Once decided, mentees can send a request 
to the selected mentor by email. 
- The selected mentor will then receive a notification email to be informed about the 
meeting request. 
- The mentee will then receive an automatically sent email from the mentor with a zoom 
link of the meeting. 
- At the selected time, mentors and mentees can join in the zoom and start the meeting.

TECH STACK: 
python, django, java, wix, css, sqlite
