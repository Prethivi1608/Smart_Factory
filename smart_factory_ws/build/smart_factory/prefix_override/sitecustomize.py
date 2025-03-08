import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = "/media/prethiviraj/R'kived Lab/Projects/2025/UTS_Robotics/Smart Factory/smart_factory_ws/install/smart_factory"
