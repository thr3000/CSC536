# CSC536
### Docker installation:
https://docs.docker.com/desktop/install/mac-install/

```
cd csc536-laravel
docker-compose build
docker-compose up -d
```
Application host on http://localhost:80

### Troubleshooting
1. 
```
ERROR: groupadd: invalid group ID 'sail'
```
Set Environment Variables Manually:
```
export WWWGROUP=1000
```

### Run Django 
1. make sure postgresql DB is on
2. Put the html file under the folder templates
```
./manage.py runserver 0.0.0.0:8000
```
3. To access login page, use URL localhost:8000/TestModel/login