import streamlit as st
import PIL.Image as Image


def init_value():
    year = [str(y) for y in range(2013, 2024)]
    default_ix = year.index("2021")
    year_choice = st.selectbox("채점을 원하시는 시험의 연도를 선택해 주세요", year, index=default_ix)

    test = ["6월", "9월", "수능"]
    test_map = {"6월": "6", "9월": "9", "수능": "f"}
    test_choice = st.selectbox("채점을 원하시는 시험을 선택해 주세요", test, index=2)

    type_ = ["확률과 통계", "미적분", "기하"] if int(year_choice) >= 2022 else ["가(A)형", "나(B)형"]
    type_map = {"확률과 통계": "p", "미적분": "c", "기하": "g", "가(A)형": "a", "나(B)형": "b"}
    type_choice = st.selectbox("채점을 원하시는 시험의 종류를 선택해 주세요", type_)

    return year_choice, test_map[test_choice], type_map[type_choice]


def show_score_img(scoring_result, inference_model, imgs_path):
    o_image = Image.open("/opt/ml/input/code/fastapi/app/scoring_image/correct.png")
    x_image = Image.open("/opt/ml/input/code/fastapi/app/scoring_image/wrong.png")
    o_width, o_height = o_image.size
    x_width, x_height = x_image.size
    exam_info = inference_model.exam_info

    for img in imgs_path:
        background = Image.open(f"/opt/ml/input/code/fastapi/app/tmp/{img}").convert(
            "RGBA"
        )
        question_ann = inference_model.load_anns_q(exam_info, img, inference_model.coco)
        for cat_id, bbox in question_ann.items():
            question = str(cat_id - 6)
            if scoring_result[question] == "O":
                background.paste(
                    o_image,
                    (
                        int(bbox[0] - o_width / 2),
                        int(bbox[1] - o_height / 2) + 10,
                    ),
                    o_image,
                )
            elif scoring_result[question] == "X":
                background.paste(
                    x_image,
                    (
                        int(bbox[0] - x_width / 2),
                        int(bbox[1] - x_height / 2) + 10,
                    ),
                    x_image,
                )
        st.image(np.array(background))
