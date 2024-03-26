# CSC536
### Docker installation:
https://docs.docker.com/desktop/install/mac-install/

### Run Django
1.
Turn on your Postgresql
enter your password on terminal
```
export DATABASE_PASSWORD=XXXX(Your password)
```
```
docker build -t csc536django .
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
