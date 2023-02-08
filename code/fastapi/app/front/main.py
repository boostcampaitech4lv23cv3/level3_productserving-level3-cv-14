import streamlit as st
import requests
import sys
from stqdm import stqdm
import io

sys.path.append("/opt/ml/input/code/fastapi/app/front")
from utils import *
from argparse import ArgumentParser


def main(args):
    st.set_page_config(layout="wide")
    st.title("몇점일까?")
    st.subheader("평가원 객관식 문제 자동채점 프로그램")
    backend_server = args.BackendServer
    year_choice, test_choice, type_choice = init_value()
    exam_info = year_choice + "_" + test_choice + "_" + type_choice
    uploaded_file = st.file_uploader("손으로 풀이된 시험지의 pdf파일을 업로드하세요.", type=["pdf"])

    if uploaded_file:
        length = 1
        files = {"file": uploaded_file.getvalue()}
        progress = stqdm(total=length)
        user_solution = requests.post(
            f"http://{backend_server}/predict/{exam_info}", files=files
        )
        progress.update(1)
        st.download_button(
            "Download Scored Image",
            data=io.BytesIO(user_solution.content).read(),
            file_name="scoring.pdf",
            mime="application/octet-stream",
        )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--BackendServer", type=str, default="34.64.169.3:30002")
    args = parser.parse_args()
    main(args)
