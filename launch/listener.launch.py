from launch import LaunchDescription
form launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener',
            output="screen"
        )
    ])