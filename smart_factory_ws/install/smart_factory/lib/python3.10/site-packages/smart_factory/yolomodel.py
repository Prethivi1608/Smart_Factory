from ultralytics import YOLO


model = YOLO('yolo11n.pt')

model.train(data='/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/RS2-hardware-Model.v2i.yolov11/data.yaml',epochs=75,imgsz=640)

model.save('/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/yolo_model/rs2_hardware_v2.pt')