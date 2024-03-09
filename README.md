# CSC536
### Docker installation:
https://docs.docker.com/desktop/install/mac-install/

```
docker-compose build
docker-compose up -d

#### for Laravel:
npm install
npm run dev
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
2.
```
ERROR: load metadata...
```
```
rm  ~/.docker/config.json
```