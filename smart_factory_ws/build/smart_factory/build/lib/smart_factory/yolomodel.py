from ultralytics import YOLO


model = YOLO('yolo11n.pt')

model.train(data='/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/smart_factory.v1i.yolov11/data.yaml',epochs=60,imgsz=640)

model.save('/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/smart_fact.pt')