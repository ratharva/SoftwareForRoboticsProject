// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from jackal_msgs:msg/StopStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "jackal_msgs/msg/detail/stop_status__rosidl_typesupport_introspection_c.h"
#include "jackal_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "jackal_msgs/msg/detail/stop_status__functions.h"
#include "jackal_msgs/msg/detail/stop_status__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void StopStatus__rosidl_typesupport_introspection_c__StopStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  jackal_msgs__msg__StopStatus__init(message_memory);
}

void StopStatus__rosidl_typesupport_introspection_c__StopStatus_fini_function(void * message_memory)
{
  jackal_msgs__msg__StopStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(jackal_msgs__msg__StopStatus, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stop_power_status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(jackal_msgs__msg__StopStatus, stop_power_status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "external_stop_present",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(jackal_msgs__msg__StopStatus, external_stop_present),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_members = {
  "jackal_msgs__msg",  // message namespace
  "StopStatus",  // message name
  3,  // number of fields
  sizeof(jackal_msgs__msg__StopStatus),
  StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_member_array,  // message members
  StopStatus__rosidl_typesupport_introspection_c__StopStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  StopStatus__rosidl_typesupport_introspection_c__StopStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_type_support_handle = {
  0,
  &StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_jackal_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, jackal_msgs, msg, StopStatus)() {
  StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_type_support_handle.typesupport_identifier) {
    StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &StopStatus__rosidl_typesupport_introspection_c__StopStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
