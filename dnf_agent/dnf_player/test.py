from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train3/weights/best.pt")  # pretrained YOLOv8n model


# Run batched inference on a list of images
results = model.predict(["img2.jpg"],conf=0.2,device="cuda")  # return a list of Results objects
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for cl  assification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk



# from roboflow import Roboflow
# rf = Roboflow(api_key="JE2dF9UuZAK1IG3GtInx")
# project = rf.workspace().project("dnf_agent")
# model = project.version("1").model
# #
# # # infer on a local image
# predict = model.predict("img.jpg", confidence=40, overlap=30).save("prediction.jpg")
