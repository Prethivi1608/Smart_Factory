import cv2
def captureImage():
    camera_name = 0
    vedioCapture = cv2.VideoCapture(camera_name)
    
    num_images = 500
    file_path = "/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/src/smart_factory/object_images/"
    
    for i in range(num_images):
        success,frame = vedioCapture.read()
    
        if success == True:
            file_name = f'{file_path}image_file{i}.jpg'
            cv2.imwrite(file_name,frame)
            cv2.waitKey(2)
            print(f"Saved {i} images")
                
    
    vedioCapture.release()

cv2.destroyAllWindows()


def main():
    captureImage()
    
    
if __name__ == '__main__':
    main()

        