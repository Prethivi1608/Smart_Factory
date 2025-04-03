from ultralytics import YOLO


model = YOLO('yolo11n.pt')

model.train(data='/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/RS2-hardware-Model.v1i.yolov11/data.yaml',epochs=60,imgsz=640)

model.save('/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/rs2_hardware.pt')