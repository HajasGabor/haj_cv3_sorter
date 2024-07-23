import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class ArraySorterNode(Node):
    def __init__(self):
        super().__init__('array_sorter')
        


def main(args=None):
    rclpy.init(args=args)
    array_sorter = ArraySorterNode()
    rclpy.spin(array_sorter)
    array_sorter.destroy_node
    rclpy.shutdown()

if __name__ == "__main__":
    main()
