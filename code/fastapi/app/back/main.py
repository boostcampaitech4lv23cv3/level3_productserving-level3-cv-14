from pathlib import Path
import pandas as pd
import io
from fastapi import FastAPI, UploadFile, File, Response, HTTPException
from fastapi.param_functions import Depends
from pydantic import Json
from pdf2image import convert_from_bytes
from mmdet.apis import init_detector
from mmdeploy_python import Detector
import numpy as np
import sys

sys.path.append("/opt/ml/input/code/fastapi/app/back")
from inference import *
from utils import *

from database import *
import os
from datetime import datetime

app = FastAPI()
detector = Detector(
    model_path="../../../data/models/on-device-model2",
    device_name="cpu",
)


@app.post("/predict/{exam_info}")
def predict(exam_info: str, file: UploadFile = File(...)):
    answer, q_bbox, img_shape = get_info_from_db(exam_info)
    images = convert_from_bytes(file.file._file.read(), dpi=100)

    images_np = [np.array(image) for image in images]
    infer_time = str(datetime.now()).replace(" ", "_")

    if not os.path.isdir(f"/opt/ml/input/code/fastapi/app/log/{infer_time}"):
        os.mkdir(f"/opt/ml/input/code/fastapi/app/log/{infer_time}")

    for idx in range(len(images_np)):
        Image.fromarray(images_np[idx]).save(
            f"/opt/ml/input/code/fastapi/app/log/{infer_time}/{idx}_original.jpg",
            "JPEG",
        )

    inference = InferenceOnDevice(
        images=images_np,
        detector=detector,
        q_bbox=q_bbox,
        answer=answer,
        img_shape=img_shape,
        time=infer_time,
    )
    scoring_img, log_pred = inference.main()
    insert_log(log_pred, exam_info, infer_time)

    imgByteArr = io.BytesIO()
    scoring_img[0].save(
        imgByteArr, save_all=True, append_images=scoring_img[1:], format="PDF"
    )

    return Response(imgByteArr.getvalue(), media_type="application/pdf")
