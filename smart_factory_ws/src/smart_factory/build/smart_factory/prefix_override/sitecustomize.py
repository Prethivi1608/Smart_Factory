import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prethivi/ros2_ws/Smart_Factory/smart_factory_ws/src/smart_factory/install/smart_factory'
