// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from jackal_msgs:msg/Drive.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "jackal_msgs/msg/detail/drive__rosidl_typesupport_introspection_c.h"
#include "jackal_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "jackal_msgs/msg/detail/drive__functions.h"
#include "jackal_msgs/msg/detail/drive__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Drive__rosidl_typesupport_introspection_c__Drive_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  jackal_msgs__msg__Drive__init(message_memory);
}

void Drive__rosidl_typesupport_introspection_c__Drive_fini_function(void * message_memory)
{
  jackal_msgs__msg__Drive__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Drive__rosidl_typesupport_introspection_c__Drive_message_member_array[2] = {
  {
    "mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(jackal_msgs__msg__Drive, mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "drivers",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    2,  // array size
    false,  // is upper bound
    offsetof(jackal_msgs__msg__Drive, drivers),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Drive__rosidl_typesupport_introspection_c__Drive_message_members = {
  "jackal_msgs__msg",  // message namespace
  "Drive",  // message name
  2,  // number of fields
  sizeof(jackal_msgs__msg__Drive),
  Drive__rosidl_typesupport_introspection_c__Drive_message_member_array,  // message members
  Drive__rosidl_typesupport_introspection_c__Drive_init_function,  // function to initialize message memory (memory has to be allocated)
  Drive__rosidl_typesupport_introspection_c__Drive_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Drive__rosidl_typesupport_introspection_c__Drive_message_type_support_handle = {
  0,
  &Drive__rosidl_typesupport_introspection_c__Drive_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_jackal_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, jackal_msgs, msg, Drive)() {
  if (!Drive__rosidl_typesupport_introspection_c__Drive_message_type_support_handle.typesupport_identifier) {
    Drive__rosidl_typesupport_introspection_c__Drive_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Drive__rosidl_typesupport_introspection_c__Drive_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
