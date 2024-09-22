from roboflow import Roboflow

rf = Roboflow(api_key="JE2dF9UuZAK1IG3GtInx")
project = rf.workspace().project("dnf_agent")

version = project.version(4)
version.deploy("yolov8", "runs/detect/train4/weights/", "best.pt")
