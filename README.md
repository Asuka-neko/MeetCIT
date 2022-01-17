# MeetCIT

### Basic Information

**TEAM MEMBERS:** 

Donglun He, Wenyi Huang, Yao Jiang, Shufan Liu, Mingxin Xue

**PROJECT NAME:** 

MeetCIT

**PROJECT OBJECTIVE:** 

Design an appointment booking website for MCIT students, where users can freely host an appointment or book another user's appointment, and meetup through the zoom link provided by the host. 

The purpose of meeting can be mentorship, advisory, mock interview or just casual meetup, to broaden the student's connection with fellow MCIT students.

**TECH STACKS:** 

- Django web framework (4.0.1), with Guardians package
- Python as back-end programming langauge
- CSS Bootstrap-4
- [django-calendar](https://github.com/huiwenhw/django-calendar) GitHub project made by GitHub user [huiwenhw](https://github.com/huiwenhw)

**For comprehensive website features**, please refer to the Feature doc.md file.

### Local Deployment Guide

1. Go to the [MeetCIT's GitHub page](https://github.com/Asuka-neko/MeetCIT) and download all resources

2. Install Python 3 [here](https://www.python.org/downloads/)

3. Open terminal and run the following command to install all required components: 

   ```
   pip install -r /path/to/requirements.txt
   ```

4. Using your terminal to cd to the MeetCIT directory that contains the 'manage.py' file

5. Run the following commands in your terminal

   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```

6. Open your browser and go to http://localhost:8000/
7. MeetCIT website is now running locally on your PC!
