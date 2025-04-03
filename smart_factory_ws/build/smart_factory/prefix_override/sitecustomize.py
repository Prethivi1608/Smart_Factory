import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prethiviraj/ros2/workspaces/Smart_Factory/smart_factory_ws/install/smart_factory'
