from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription


def generate_launch_description():
    use_hardware = LaunchConfiguration('use_hardware')
    declare_hw = DeclareLaunchArgument('use_hardware', default_value='true')

    moveit_config = (
        MoveItConfigsBuilder("fairino5_v6_robot", package_name="fairino5_v6_moveit2_config")
        .robot_description(mappings={'use_hardware': use_hardware})
        .to_moveit_configs()
    )
    demo_ld = generate_demo_launch(moveit_config)
    # Prepend the argument declaration to the generated launch
    return LaunchDescription([declare_hw, *demo_ld.entities])
