## Prepare
1. 모델 불러오기
~~~
dvc pull data/models/on-device-model2
~~~

2. db_secrets.json 저장 \
path : code/fastapi/app/back/db_secrets.json

3. docker-compose.yaml front command 변경 \
{server ip}:{port} -> 자신의 backend server

## command
~~~
docker-compose up
~~~