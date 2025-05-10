# generated from rosidl_generator_py/resource/_idl.py.em
# with input from smart_factory_services:srv/TaskAllocation.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TaskAllocation_Request(type):
    """Metaclass of message 'TaskAllocation_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('smart_factory_services')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'smart_factory_services.srv.TaskAllocation_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__task_allocation__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__task_allocation__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__task_allocation__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__task_allocation__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__task_allocation__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TaskAllocation_Request(metaclass=Metaclass_TaskAllocation_Request):
    """Message class 'TaskAllocation_Request'."""

    __slots__ = [
        '_robot_number',
    ]

    _fields_and_field_types = {
        'robot_number': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.robot_number = kwargs.get('robot_number', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.robot_number != other.robot_number:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def robot_number(self):
        """Message field 'robot_number'."""
        return self._robot_number

    @robot_number.setter
    def robot_number(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot_number' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'robot_number' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._robot_number = value


# Import statements for member types

# Member 'goal_points'
import array  # noqa: E402, I100

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_TaskAllocation_Response(type):
    """Metaclass of message 'TaskAllocation_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('smart_factory_services')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'smart_factory_services.srv.TaskAllocation_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__task_allocation__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__task_allocation__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__task_allocation__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__task_allocation__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__task_allocation__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TaskAllocation_Response(metaclass=Metaclass_TaskAllocation_Response):
    """Message class 'TaskAllocation_Response'."""

    __slots__ = [
        '_success',
        '_object_name',
        '_message',
        '_available_goals',
        '_goal_points',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'object_name': 'string',
        'message': 'string',
        'available_goals': 'int64',
        'goal_points': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.object_name = kwargs.get('object_name', str())
        self.message = kwargs.get('message', str())
        self.available_goals = kwargs.get('available_goals', int())
        self.goal_points = array.array('d', kwargs.get('goal_points', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.object_name != other.object_name:
            return False
        if self.message != other.message:
            return False
        if self.available_goals != other.available_goals:
            return False
        if self.goal_points != other.goal_points:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def object_name(self):
        """Message field 'object_name'."""
        return self._object_name

    @object_name.setter
    def object_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'object_name' field must be of type 'str'"
        self._object_name = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value

    @builtins.property
    def available_goals(self):
        """Message field 'available_goals'."""
        return self._available_goals

    @available_goals.setter
    def available_goals(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'available_goals' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'available_goals' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._available_goals = value

    @builtins.property
    def goal_points(self):
        """Message field 'goal_points'."""
        return self._goal_points

    @goal_points.setter
    def goal_points(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'goal_points' array.array() must have the type code of 'd'"
            self._goal_points = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'goal_points' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._goal_points = array.array('d', value)


class Metaclass_TaskAllocation(type):
    """Metaclass of service 'TaskAllocation'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('smart_factory_services')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'smart_factory_services.srv.TaskAllocation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__task_allocation

            from smart_factory_services.srv import _task_allocation
            if _task_allocation.Metaclass_TaskAllocation_Request._TYPE_SUPPORT is None:
                _task_allocation.Metaclass_TaskAllocation_Request.__import_type_support__()
            if _task_allocation.Metaclass_TaskAllocation_Response._TYPE_SUPPORT is None:
                _task_allocation.Metaclass_TaskAllocation_Response.__import_type_support__()


class TaskAllocation(metaclass=Metaclass_TaskAllocation):
    from smart_factory_services.srv._task_allocation import TaskAllocation_Request as Request
    from smart_factory_services.srv._task_allocation import TaskAllocation_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
