// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from smart_factory_services:srv/TaskAllocation.idl
// generated code does not contain a copyright notice

#ifndef SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_HPP_
#define SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__smart_factory_services__srv__TaskAllocation_Request __attribute__((deprecated))
#else
# define DEPRECATED__smart_factory_services__srv__TaskAllocation_Request __declspec(deprecated)
#endif

namespace smart_factory_services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskAllocation_Request_
{
  using Type = TaskAllocation_Request_<ContainerAllocator>;

  explicit TaskAllocation_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_number = 0ll;
      this->object_name = "";
    }
  }

  explicit TaskAllocation_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : object_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_number = 0ll;
      this->object_name = "";
    }
  }

  // field types and members
  using _robot_number_type =
    int64_t;
  _robot_number_type robot_number;
  using _object_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _object_name_type object_name;

  // setters for named parameter idiom
  Type & set__robot_number(
    const int64_t & _arg)
  {
    this->robot_number = _arg;
    return *this;
  }
  Type & set__object_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->object_name = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__smart_factory_services__srv__TaskAllocation_Request
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__smart_factory_services__srv__TaskAllocation_Request
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskAllocation_Request_ & other) const
  {
    if (this->robot_number != other.robot_number) {
      return false;
    }
    if (this->object_name != other.object_name) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskAllocation_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskAllocation_Request_

// alias to use template instance with default allocator
using TaskAllocation_Request =
  smart_factory_services::srv::TaskAllocation_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace smart_factory_services


#ifndef _WIN32
# define DEPRECATED__smart_factory_services__srv__TaskAllocation_Response __attribute__((deprecated))
#else
# define DEPRECATED__smart_factory_services__srv__TaskAllocation_Response __declspec(deprecated)
#endif

namespace smart_factory_services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskAllocation_Response_
{
  using Type = TaskAllocation_Response_<ContainerAllocator>;

  explicit TaskAllocation_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit TaskAllocation_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__smart_factory_services__srv__TaskAllocation_Response
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__smart_factory_services__srv__TaskAllocation_Response
    std::shared_ptr<smart_factory_services::srv::TaskAllocation_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskAllocation_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskAllocation_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskAllocation_Response_

// alias to use template instance with default allocator
using TaskAllocation_Response =
  smart_factory_services::srv::TaskAllocation_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace smart_factory_services

namespace smart_factory_services
{

namespace srv
{

struct TaskAllocation
{
  using Request = smart_factory_services::srv::TaskAllocation_Request;
  using Response = smart_factory_services::srv::TaskAllocation_Response;
};

}  // namespace srv

}  // namespace smart_factory_services

#endif  // SMART_FACTORY_SERVICES__SRV__DETAIL__TASK_ALLOCATION__STRUCT_HPP_
