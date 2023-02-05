export ONNXRUNTIME_DIR=/opt/ml/input/onnxruntime-linux-x64-1.8.1 &&\
export LD_LIBRARY_PATH=$ONNXRUNTIME_DIR/lib:$LD_LIBRARY_PATH &&\
python3 app/back/main.py 