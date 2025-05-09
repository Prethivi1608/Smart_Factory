// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice
#include "smart_factory_services/srv/detail/task_allocation__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "smart_factory_services/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "smart_factory_services/srv/detail/task_allocation__struct.h"
#include "smart_factory_services/srv/detail/task_allocation__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TaskAllocation_Request__ros_msg_type = smart_factory_services__srv__TaskAllocation_Request;

static bool _TaskAllocation_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TaskAllocation_Request__ros_msg_type * ros_message = static_cast<const _TaskAllocation_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: robot_number
  {
    cdr << ros_message->robot_number;
  }

  return true;
}

static bool _TaskAllocation_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TaskAllocation_Request__ros_msg_type * ros_message = static_cast<_TaskAllocation_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: robot_number
  {
    cdr >> ros_message->robot_number;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smart_factory_services
size_t get_serialized_size_smart_factory_services__srv__TaskAllocation_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TaskAllocation_Request__ros_msg_type * ros_message = static_cast<const _TaskAllocation_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name robot_number
  {
    size_t item_size = sizeof(ros_message->robot_number);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TaskAllocation_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_smart_factory_services__srv__TaskAllocation_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smart_factory_services
size_t max_serialized_size_smart_factory_services__srv__TaskAllocation_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: robot_number
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = smart_factory_services__srv__TaskAllocation_Request;
    is_plain =
      (
      offsetof(DataType, robot_number) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TaskAllocation_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_smart_factory_services__srv__TaskAllocation_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TaskAllocation_Request = {
  "smart_factory_services::srv",
  "TaskAllocation_Request",
  _TaskAllocation_Request__cdr_serialize,
  _TaskAllocation_Request__cdr_deserialize,
  _TaskAllocation_Request__get_serialized_size,
  _TaskAllocation_Request__max_serialized_size
};

static rosidl_message_type_support_t _TaskAllocation_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TaskAllocation_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smart_factory_services, srv, TaskAllocation_Request)() {
  return &_TaskAllocation_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "smart_factory_services/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__struct.h"
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // goal_points
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // goal_points
#include "rosidl_runtime_c/string.h"  // message, object_name
#include "rosidl_runtime_c/string_functions.h"  // message, object_name

// forward declare type support functions


using _TaskAllocation_Response__ros_msg_type = smart_factory_services__srv__TaskAllocation_Response;

static bool _TaskAllocation_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TaskAllocation_Response__ros_msg_type * ros_message = static_cast<const _TaskAllocation_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  // Field name: object_name
  {
    const rosidl_runtime_c__String * str = &ros_message->object_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: message
  {
    const rosidl_runtime_c__String * str = &ros_message->message;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: available_goals
  {
    cdr << ros_message->available_goals;
  }

  // Field name: goal_points
  {
    size_t size = ros_message->goal_points.size;
    auto array_ptr = ros_message->goal_points.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _TaskAllocation_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TaskAllocation_Response__ros_msg_type * ros_message = static_cast<_TaskAllocation_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  // Field name: object_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->object_name.data) {
      rosidl_runtime_c__String__init(&ros_message->object_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->object_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'object_name'\n");
      return false;
    }
  }

  // Field name: message
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->message.data) {
      rosidl_runtime_c__String__init(&ros_message->message);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->message,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'message'\n");
      return false;
    }
  }

  // Field name: available_goals
  {
    cdr >> ros_message->available_goals;
  }

  // Field name: goal_points
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->goal_points.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->goal_points);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->goal_points, size)) {
      fprintf(stderr, "failed to create array for field 'goal_points'");
      return false;
    }
    auto array_ptr = ros_message->goal_points.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smart_factory_services
size_t get_serialized_size_smart_factory_services__srv__TaskAllocation_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TaskAllocation_Response__ros_msg_type * ros_message = static_cast<const _TaskAllocation_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name object_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->object_name.size + 1);
  // field.name message
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->message.size + 1);
  // field.name available_goals
  {
    size_t item_size = sizeof(ros_message->available_goals);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name goal_points
  {
    size_t array_size = ros_message->goal_points.size;
    auto array_ptr = ros_message->goal_points.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TaskAllocation_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_smart_factory_services__srv__TaskAllocation_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smart_factory_services
size_t max_serialized_size_smart_factory_services__srv__TaskAllocation_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: object_name
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: message
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: available_goals
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: goal_points
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = smart_factory_services__srv__TaskAllocation_Response;
    is_plain =
      (
      offsetof(DataType, goal_points) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TaskAllocation_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_smart_factory_services__srv__TaskAllocation_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TaskAllocation_Response = {
  "smart_factory_services::srv",
  "TaskAllocation_Response",
  _TaskAllocation_Response__cdr_serialize,
  _TaskAllocation_Response__cdr_deserialize,
  _TaskAllocation_Response__get_serialized_size,
  _TaskAllocation_Response__max_serialized_size
};

static rosidl_message_type_support_t _TaskAllocation_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TaskAllocation_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smart_factory_services, srv, TaskAllocation_Response)() {
  return &_TaskAllocation_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "smart_factory_services/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "smart_factory_services/srv/task_allocation.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t TaskAllocation__callbacks = {
  "smart_factory_services::srv",
  "TaskAllocation",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smart_factory_services, srv, TaskAllocation_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smart_factory_services, srv, TaskAllocation_Response)(),
};

static rosidl_service_type_support_t TaskAllocation__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &TaskAllocation__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smart_factory_services, srv, TaskAllocation)() {
  return &TaskAllocation__handle;
}

#if defined(__cplusplus)
}
#endif
