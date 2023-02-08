## Prepare
1. 모델 불러오기
~~~
dvc pull data/models/on-device-model2.dvc
~~~

2. db_secrets.json 저장 \
path : code/fastapi/app/back/db_secrets.json

3. docker-compose.yaml front command 변경 \
{server ip}:{port} -> 자신의 backend server

## command
~~~
docker-compose up
~~~

## reference
on-device branch의 코드는 [V-1.0](https://github.com/boostcampaitech4lv23cv3/level3_productserving-level3-cv-14/tree/V-1.0)을 기준으로 작성되었습니다.