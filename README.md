# BoostCamp AI Tech4 Final-Project-CV-14 ๋ช์ ์ผ๊น?

## <br/> Member๐ฅ

| [๊น์งํ](https://github.com/kzh3010) | [์์ค์](https://github.com/JSJSWON) | [์ก์์ญ](https://github.com/gih0109) | [ํ๊ฑดํ](https://github.com/GeonHyeock) | [ํ์ฃผ์](https://github.com/archemist-hong) |
| :-: | :-: | :-: | :-: | :-: |
| <img src="https://avatars.githubusercontent.com/kzh3010" width="100"> | <img src="https://avatars.githubusercontent.com/JSJSWON" width="100"> | <img src="https://avatars.githubusercontent.com/gih0109" width="100"> | <img src="https://avatars.githubusercontent.com/GeonHyeock" width="100"> | <img src="https://avatars.githubusercontent.com/archemist-hong" width="100"> |


## <br/>๐ฏ ํ๋ก์ ํธ ์๊ฐ

### - Purpose
์ฑ์ ์ ๋จ์ ๋ฐ๋ณต ์๋ฌด์ด๋ฉด์, ์๊ฐ์ด ์ค๋ ๊ฑธ๋ฆฌ๋ ํผ๊ณคํ๊ณ  ๊ท์ฐฎ์ ์ผ์๋๋ค. ๊ฒ๋ค๊ฐ ์ฑ์ ์ ํ๋ค ๋ณด๋ฉด ๋, ํ๋ฆฌ ๋ฑ์ ํผ๋ก๋์ ๋ฐ๋ผ ์ค์๊ฐ ๋ฐ์ํ  ์ ์๋ ์๋ฌด์ด๊ธฐ๋ ํฉ๋๋ค. 

์ด๋ฌํ ๋จ์ ๋ฐ๋ณต ์๋ฌด๋ฅผ ๋ฅ๋ฌ๋์ ์ด์ฉํ์ฌ ์ฌ๋์ ๋ธ๋๋ ฅ์ ์ค์ด๊ณ  ์ ํ๋์ ์๋ ์ธก๋ฉด์์ ๋ฅ๋ฅ ์ ์ฌ๋ฆฌ๊ธฐ ์ํด ์๋น์ค๋ฅผ ์ ์ํ์์ต๋๋ค.

### - Expectations
์ฌ์  ์กฐ์ฌ๋ฅผ ํตํด ์ต๊ทผ ํ์๋ค์ด ์ค๋งํธ ๋๋ฐ์ด์ค๋ฅผ ํตํด ์ํ์ง๋ฅผ ํธ๋ ๊ฒฝ์ฐ๊ฐ ๋ง๋ค๋ ๊ฒ์ ์๊ฒ ๋์์ต๋๋ค. 

์ด ์๋น์ค๋ ์ค๋งํธ ๋๋ฐ์ด์ค์์ ํ์์ด ์์ผ๋ก ํ์ดํ ์ํ์ง๋ฅผ ์ถ๊ฐ์ ์ธ ๋ธ๋๋ ฅ ์์ด ๋น ๋ฅด๊ณ  ์ ํํ๊ฒ ์ฑ์ ํ  ์๋ AI ํ์ต ๋ณด์กฐ ๋๊ตฌ๋ก์์ ์ญํ ์ ํ๋๋ก ํ๊ณ ์ ํฉ๋๋ค.


## <br/>๐ Project Overview

- ํ๋ก์ ํธ ์ํ ๊ธฐ๊ฐ : 2023.01.09. ~ 2023.02.09.
- ๋ฐํ ์์: [Link](https://youtu.be/K58zIGAeKP8)
- ๋ฐํ ์๋ฃ: [Link](https://drive.google.com/file/d/19-3Co7l_IogkPFJwmyt27zMFkGrljhQs/view?usp=sharing)
- ํ๋ก์ ํธ ์๊ฐ : [Link](https://whatsthescore.notion.site/751cae9de62c4603b6bc26fbb71eb156)

## <br/>๐ฅ ๋ฐ๋ชจ ์์

<img src="https://user-images.githubusercontent.com/40621526/217222547-6c99e748-7ebb-46df-a037-c2e3d38271e9.gif">


## <br/>๐๏ธ Data set
 
- Annotation
    - Hasty annotation tool
    - ํ๊ฐ์ ์๋ฅ ์ํ ๋ชจ์๊ณ ์ฌ 11๊ฐ๋ 768์ฅ
- Synthetic Data 
    - ์๋ณธ ๋ฐ์ดํฐ + [CROHME](https://www.isical.ac.in/~crohme/) ์ ํ๊ธฐ ์์ ๋ฐ์ดํฐ + ์ง์  ์ ์ํ ์ฒดํฌ ํ์ ์ด๋ฏธ์ง ๋ฐ์ดํฐ
- ๋ฐ์ดํฐ ๊ด๋ฆฌ
    - DVC(Data Version Control)
    - ๊ตฌ๊ธ ๋๋ผ์ด๋ธ API 


## <br/>๐งค Flow Chart

<img src="./Readme-image/model_pipline.jpg" >

- input 
    - ํ์๋ค์ด ํ์ดํ ์ํ์ง pdf ํ์ผ
- Detection 
    - ๊ฐ๊ด์ ๋ณด๊ธฐ ๋ฐ ์ฃผ๊ด์ ์ ๋ต Detection
- Text recognition
    - Detection ๋ ์ฃผ๊ด์ ์ ๋ต์ recognition
- ์ฑ์ 
    - DB์ ์ ์ฅ๋ ์ ๋ต๊ณผ ๋น๊ต ํ ์ฑ์ 


## <br/>๐ฉ Demo Page Structure

<img src="./Readme-image/serving_img2.jpg" >

- Frontend - Streamlit(Html,CSS)
- Backend - FastAPI 
- DataBase - PostgreSQL
- Docker
- Google Cloud Platform

## <br/>๐ฑ On-Device
- Frontend์ Backend๋ถ๋ถ์ Dockerfile์ ์์ฑํ์ฌ ์ด๋ฅผ ๋ฐํ์ผ๋ก docker-compose๋ฅผ ์ด์ฉํด ๋น ๋ฅด๊ฒ building ํ  ์ ์์ต๋๋ค.
- [On-Device Branch](https://github.com/boostcampaitech4lv23cv3/level3_productserving-level3-cv-14/tree/on-device)


## <br/>๐ Future Research

- inference time ๋จ์ถ
- Mobile Application ์ ์
- jpg ๋ฑ๊ณผ ๊ฐ์ ์ด๋ฏธ์ง ํ์ผ ์ ์ฉ
- ๊ธฐ๋ฅ ๊ฐ๋ฐ(์ํ ๊ณผ๋ชฉ ํ์ฅ, ์ ์ฌ๋ฌธ์  ์ถ์ฒ, ํด์ค ์ ๊ณต ๋ฑ)

## <br/>๐ Reference

- [Mmdetection](https://github.com/open-mmlab/mmdetection)
- [Cascade R-CNN](https://arxiv.org/abs/1712.00726)
- [ConvNeXt](https://github.com/facebookresearch/ConvNeXt)
- [Clovaai : TPS-ResNet-BiLSTM-Attn](https://github.com/clovaai/deep-text-recognition-benchmark)
- [๋ชจ์_๋ชจ๋์ ์ํ](https://blog.naver.com/math4x/222574149191)
- [ํ๊ตญ๊ต์ก๊ณผ์ ํ๊ฐ์](https://www.suneung.re.kr/boardCnts/list.do?boardID=1500234&m=0403&s=suneung&searchStr=)
