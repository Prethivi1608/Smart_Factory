// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice

#ifndef SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__TRAITS_HPP_
#define SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "smart_factory_services/srv/detail/task_allocation__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace smart_factory_services
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskAllocation_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_number
  {
    out << "robot_number: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_number, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskAllocation_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_number: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_number, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskAllocation_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace smart_factory_services

namespace rosidl_generator_traits
{

[[deprecated("use smart_factory_services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const smart_factory_services::srv::TaskAllocation_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  smart_factory_services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use smart_factory_services::srv::to_yaml() instead")]]
inline std::string to_yaml(const smart_factory_services::srv::TaskAllocation_Request & msg)
{
  return smart_factory_services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<smart_factory_services::srv::TaskAllocation_Request>()
{
  return "smart_factory_services::srv::TaskAllocation_Request";
}

template<>
inline const char * name<smart_factory_services::srv::TaskAllocation_Request>()
{
  return "smart_factory_services/srv/TaskAllocation_Request";
}

template<>
struct has_fixed_size<smart_factory_services::srv::TaskAllocation_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<smart_factory_services::srv::TaskAllocation_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<smart_factory_services::srv::TaskAllocation_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace smart_factory_services
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskAllocation_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: object_name
  {
    out << "object_name: ";
    rosidl_generator_traits::value_to_yaml(msg.object_name, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskAllocation_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: object_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "object_name: ";
    rosidl_generator_traits::value_to_yaml(msg.object_name, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskAllocation_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace smart_factory_services

namespace rosidl_generator_traits
{

[[deprecated("use smart_factory_services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const smart_factory_services::srv::TaskAllocation_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  smart_factory_services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use smart_factory_services::srv::to_yaml() instead")]]
inline std::string to_yaml(const smart_factory_services::srv::TaskAllocation_Response & msg)
{
  return smart_factory_services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<smart_factory_services::srv::TaskAllocation_Response>()
{
  return "smart_factory_services::srv::TaskAllocation_Response";
}

template<>
inline const char * name<smart_factory_services::srv::TaskAllocation_Response>()
{
  return "smart_factory_services/srv/TaskAllocation_Response";
}

template<>
struct has_fixed_size<smart_factory_services::srv::TaskAllocation_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<smart_factory_services::srv::TaskAllocation_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<smart_factory_services::srv::TaskAllocation_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<smart_factory_services::srv::TaskAllocation>()
{
  return "smart_factory_services::srv::TaskAllocation";
}

template<>
inline const char * name<smart_factory_services::srv::TaskAllocation>()
{
  return "smart_factory_services/srv/TaskAllocation";
}

template<>
struct has_fixed_size<smart_factory_services::srv::TaskAllocation>
  : std::integral_constant<
    bool,
    has_fixed_size<smart_factory_services::srv::TaskAllocation_Request>::value &&
    has_fixed_size<smart_factory_services::srv::TaskAllocation_Response>::value
  >
{
};

template<>
struct has_bounded_size<smart_factory_services::srv::TaskAllocation>
  : std::integral_constant<
    bool,
    has_bounded_size<smart_factory_services::srv::TaskAllocation_Request>::value &&
    has_bounded_size<smart_factory_services::srv::TaskAllocation_Response>::value
  >
{
};

template<>
struct is_service<smart_factory_services::srv::TaskAllocation>
  : std::true_type
{
};

template<>
struct is_service_request<smart_factory_services::srv::TaskAllocation_Request>
  : std::true_type
{
};

template<>
struct is_service_response<smart_factory_services::srv::TaskAllocation_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__TRAITS_HPP_
