import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
    # Get the path to the Jackal and accessory URDF files
    jackal_description_path = os.path.join(get_package_share_directory('jackal_description'), 'urdf', 'jackal.urdf.xacro')
    camera_description_path = os.path.join(get_package_share_directory('my_robot'), 'urdf', 'stereo_camera_mount.urdf.xacro')

    # Declare the launch arguments
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true')
    world_arg = DeclareLaunchArgument('world', default_value=os.path.join(get_package_share_directory('my_robot'), 'worlds', 'empty.world'))

    # Spawn the Jackal and accessory URDF files
    jackal_spawner = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'jackal', '-file', jackal_description_path]
    )

    camera_spawner = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'camera', '-file', camera_description_path]
    )

    # Publish the robot's joint states
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        arguments=[jackal_description_path]
    )

    # Configure the camera joint limits and controllers
    camera_controller = Node(
        package='my_robot',
        executable='camera_controller',
        output='screen'
    )

    return LaunchDescription([
        use_sim_time_arg,
        world_arg,
        jackal_spawner,
        camera_spawner,
        robot_state_publisher,
        camera_controller
    ])