from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # build a new model from scratch

# Use the model
model.train(data="../datasets/dnf_player_dataset_v1/data.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("img.jpg")  # predict on an image
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for cl  assification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
# path = model.export(format="onnx")  # export the model to ONNX format