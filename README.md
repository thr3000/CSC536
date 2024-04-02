# CSC536

### Run Django
Turn on your Postgresql
enter your password on terminal
```
export DATABASE_PASSWORD=XXXX(Your password)
```
```
python manage.py migrate
./manage.py runserver 0.0.0.0:8000
```
Application host on http://localhost:8000/TestModel/homepage

### Troubleshooting
1. 
```
env: python: No such file or directory
```
Modify manage.py accordingly to your python version
```
#!/usr/bin/env python
or
#!/usr/bin/env python3
```