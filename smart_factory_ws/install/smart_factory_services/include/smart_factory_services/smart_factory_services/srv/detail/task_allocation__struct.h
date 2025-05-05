// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice

#ifndef SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_H_
#define SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'object_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/TaskAllocation in the package smart_factory_services.
typedef struct smart_factory_services__srv__TaskAllocation_Request
{
  int64_t robot_number;
  rosidl_runtime_c__String object_name;
} smart_factory_services__srv__TaskAllocation_Request;

// Struct for a sequence of smart_factory_services__srv__TaskAllocation_Request.
typedef struct smart_factory_services__srv__TaskAllocation_Request__Sequence
{
  smart_factory_services__srv__TaskAllocation_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} smart_factory_services__srv__TaskAllocation_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/TaskAllocation in the package smart_factory_services.
typedef struct smart_factory_services__srv__TaskAllocation_Response
{
  bool success;
  rosidl_runtime_c__String message;
} smart_factory_services__srv__TaskAllocation_Response;

// Struct for a sequence of smart_factory_services__srv__TaskAllocation_Response.
typedef struct smart_factory_services__srv__TaskAllocation_Response__Sequence
{
  smart_factory_services__srv__TaskAllocation_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} smart_factory_services__srv__TaskAllocation_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_H_
