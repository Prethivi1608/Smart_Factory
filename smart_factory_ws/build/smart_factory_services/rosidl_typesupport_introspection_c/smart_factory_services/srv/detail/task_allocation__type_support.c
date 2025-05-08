// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "smart_factory_services/srv/detail/task_allocation__rosidl_typesupport_introspection_c.h"
#include "smart_factory_services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "smart_factory_services/srv/detail/task_allocation__functions.h"
#include "smart_factory_services/srv/detail/task_allocation__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  smart_factory_services__srv__TaskAllocation_Request__init(message_memory);
}

void smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_fini_function(void * message_memory)
{
  smart_factory_services__srv__TaskAllocation_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_member_array[1] = {
  {
    "robot_number",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smart_factory_services__srv__TaskAllocation_Request, robot_number),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_members = {
  "smart_factory_services__srv",  // message namespace
  "TaskAllocation_Request",  // message name
  1,  // number of fields
  sizeof(smart_factory_services__srv__TaskAllocation_Request),
  smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_member_array,  // message members
  smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_type_support_handle = {
  0,
  &smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_smart_factory_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Request)() {
  if (!smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_type_support_handle.typesupport_identifier) {
    smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &smart_factory_services__srv__TaskAllocation_Request__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__rosidl_typesupport_introspection_c.h"
// already included above
// #include "smart_factory_services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__functions.h"
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__struct.h"


// Include directives for member types
// Member `object_name`
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  smart_factory_services__srv__TaskAllocation_Response__init(message_memory);
}

void smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_fini_function(void * message_memory)
{
  smart_factory_services__srv__TaskAllocation_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smart_factory_services__srv__TaskAllocation_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "object_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smart_factory_services__srv__TaskAllocation_Response, object_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smart_factory_services__srv__TaskAllocation_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_members = {
  "smart_factory_services__srv",  // message namespace
  "TaskAllocation_Response",  // message name
  3,  // number of fields
  sizeof(smart_factory_services__srv__TaskAllocation_Response),
  smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_member_array,  // message members
  smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_type_support_handle = {
  0,
  &smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_smart_factory_services
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Response)() {
  if (!smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_type_support_handle.typesupport_identifier) {
    smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &smart_factory_services__srv__TaskAllocation_Response__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "smart_factory_services/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "smart_factory_services/srv/detail/task_allocation__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_members = {
  "smart_factory_services__srv",  // service namespace
  "TaskAllocation",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_Request_message_type_support_handle,
  NULL  // response message
  // smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_Response_message_type_support_handle
};

static rosidl_service_type_support_t smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_type_support_handle = {
  0,
  &smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_smart_factory_services
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation)() {
  if (!smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_type_support_handle.typesupport_identifier) {
    smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, smart_factory_services, srv, TaskAllocation_Response)()->data;
  }

  return &smart_factory_services__srv__detail__task_allocation__rosidl_typesupport_introspection_c__TaskAllocation_service_type_support_handle;
}
