import os

def get_model_size(model_path):
    size_in_bytes = os.path.getsize(model_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    return size_in_mb

model_path = "/home/syj/A40_Test/inception_v1/model.onnx"

model_size_mb = get_model_size(model_path)
print(f"Model size: {model_size_mb} MB")
