# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/RoverAckermannSetpoint.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RoverAckermannSetpoint(type):
    """Metaclass of message 'RoverAckermannSetpoint'."""

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
            module = import_type_support('px4_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'px4_msgs.msg.RoverAckermannSetpoint')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__rover_ackermann_setpoint
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__rover_ackermann_setpoint
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__rover_ackermann_setpoint
            cls._TYPE_SUPPORT = module.type_support_msg__msg__rover_ackermann_setpoint
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__rover_ackermann_setpoint

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RoverAckermannSetpoint(metaclass=Metaclass_RoverAckermannSetpoint):
    """Message class 'RoverAckermannSetpoint'."""

    __slots__ = [
        '_timestamp',
        '_forward_speed_setpoint',
        '_forward_speed_setpoint_normalized',
        '_steering_setpoint',
        '_steering_setpoint_normalized',
        '_lateral_acceleration_setpoint',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'forward_speed_setpoint': 'float',
        'forward_speed_setpoint_normalized': 'float',
        'steering_setpoint': 'float',
        'steering_setpoint_normalized': 'float',
        'lateral_acceleration_setpoint': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.forward_speed_setpoint = kwargs.get('forward_speed_setpoint', float())
        self.forward_speed_setpoint_normalized = kwargs.get('forward_speed_setpoint_normalized', float())
        self.steering_setpoint = kwargs.get('steering_setpoint', float())
        self.steering_setpoint_normalized = kwargs.get('steering_setpoint_normalized', float())
        self.lateral_acceleration_setpoint = kwargs.get('lateral_acceleration_setpoint', float())

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
        if self.timestamp != other.timestamp:
            return False
        if self.forward_speed_setpoint != other.forward_speed_setpoint:
            return False
        if self.forward_speed_setpoint_normalized != other.forward_speed_setpoint_normalized:
            return False
        if self.steering_setpoint != other.steering_setpoint:
            return False
        if self.steering_setpoint_normalized != other.steering_setpoint_normalized:
            return False
        if self.lateral_acceleration_setpoint != other.lateral_acceleration_setpoint:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @builtins.property
    def forward_speed_setpoint(self):
        """Message field 'forward_speed_setpoint'."""
        return self._forward_speed_setpoint

    @forward_speed_setpoint.setter
    def forward_speed_setpoint(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'forward_speed_setpoint' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'forward_speed_setpoint' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._forward_speed_setpoint = value

    @builtins.property
    def forward_speed_setpoint_normalized(self):
        """Message field 'forward_speed_setpoint_normalized'."""
        return self._forward_speed_setpoint_normalized

    @forward_speed_setpoint_normalized.setter
    def forward_speed_setpoint_normalized(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'forward_speed_setpoint_normalized' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'forward_speed_setpoint_normalized' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._forward_speed_setpoint_normalized = value

    @builtins.property
    def steering_setpoint(self):
        """Message field 'steering_setpoint'."""
        return self._steering_setpoint

    @steering_setpoint.setter
    def steering_setpoint(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'steering_setpoint' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'steering_setpoint' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._steering_setpoint = value

    @builtins.property
    def steering_setpoint_normalized(self):
        """Message field 'steering_setpoint_normalized'."""
        return self._steering_setpoint_normalized

    @steering_setpoint_normalized.setter
    def steering_setpoint_normalized(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'steering_setpoint_normalized' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'steering_setpoint_normalized' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._steering_setpoint_normalized = value

    @builtins.property
    def lateral_acceleration_setpoint(self):
        """Message field 'lateral_acceleration_setpoint'."""
        return self._lateral_acceleration_setpoint

    @lateral_acceleration_setpoint.setter
    def lateral_acceleration_setpoint(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lateral_acceleration_setpoint' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lateral_acceleration_setpoint' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lateral_acceleration_setpoint = value
