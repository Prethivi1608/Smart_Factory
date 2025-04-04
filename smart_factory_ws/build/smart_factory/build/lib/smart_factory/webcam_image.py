import cv2
def captureImage():
    camera_name = 2
    vedioCapture = cv2.VideoCapture(camera_name)
    
    num_images = 250
    file_path = "/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/camera_webcam/"
    
    for i in range(num_images):
        success,frame = vedioCapture.read()
    
        if success == True:
            file_name = f'{file_path}image_file{i+750}.jpg'
            cv2.imwrite(file_name,frame)
            cv2.waitKey(0)
                
    
    vedioCapture.release()

cv2.destroyAllWindows()


def main():
    captureImage()
    
    
if __name__ == '__main__':
    main()