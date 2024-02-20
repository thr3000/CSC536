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
