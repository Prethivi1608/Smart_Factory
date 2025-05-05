// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice

#ifndef SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__BUILDER_HPP_
#define SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "smart_factory_services/srv/detail/task_allocation__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace smart_factory_services
{

namespace srv
{

namespace builder
{

class Init_TaskAllocation_Request_object_name
{
public:
  explicit Init_TaskAllocation_Request_object_name(::smart_factory_services::srv::TaskAllocation_Request & msg)
  : msg_(msg)
  {}
  ::smart_factory_services::srv::TaskAllocation_Request object_name(::smart_factory_services::srv::TaskAllocation_Request::_object_name_type arg)
  {
    msg_.object_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::smart_factory_services::srv::TaskAllocation_Request msg_;
};

class Init_TaskAllocation_Request_robot_number
{
public:
  Init_TaskAllocation_Request_robot_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskAllocation_Request_object_name robot_number(::smart_factory_services::srv::TaskAllocation_Request::_robot_number_type arg)
  {
    msg_.robot_number = std::move(arg);
    return Init_TaskAllocation_Request_object_name(msg_);
  }

private:
  ::smart_factory_services::srv::TaskAllocation_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::smart_factory_services::srv::TaskAllocation_Request>()
{
  return smart_factory_services::srv::builder::Init_TaskAllocation_Request_robot_number();
}

}  // namespace smart_factory_services


namespace smart_factory_services
{

namespace srv
{

namespace builder
{

class Init_TaskAllocation_Response_message
{
public:
  explicit Init_TaskAllocation_Response_message(::smart_factory_services::srv::TaskAllocation_Response & msg)
  : msg_(msg)
  {}
  ::smart_factory_services::srv::TaskAllocation_Response message(::smart_factory_services::srv::TaskAllocation_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::smart_factory_services::srv::TaskAllocation_Response msg_;
};

class Init_TaskAllocation_Response_success
{
public:
  Init_TaskAllocation_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskAllocation_Response_message success(::smart_factory_services::srv::TaskAllocation_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_TaskAllocation_Response_message(msg_);
  }

private:
  ::smart_factory_services::srv::TaskAllocation_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::smart_factory_services::srv::TaskAllocation_Response>()
{
  return smart_factory_services::srv::builder::Init_TaskAllocation_Response_success();
}

}  // namespace smart_factory_services

#endif  // SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__BUILDER_HPP_
