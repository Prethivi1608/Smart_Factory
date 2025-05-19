from ultralytics import YOLO


model = YOLO('yolo11n.pt')

model.train(data='/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/tb3-object-detection.v1i.yolov11/data.yaml',epochs=50,imgsz=640)

model.save('/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/tb3_object.pt')