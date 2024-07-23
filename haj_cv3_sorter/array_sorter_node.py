import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class ArraySorterNode(Node):
    def __init__(self):
        super().__init__('array_sorter')
        
        self.subscription_ = self.create_subscription(
            Float32MultiArray,
            'input_array',
            self.sorter_callback,
            10,
        )

        self.publisher_ = self.create_publisher(
            Float32MultiArray,
            'sorted_array',
            10,
        )
    
    def sorter_callback(self, msg):
        sorted_array = sorted(msg.data)
        sorted_msg = Float32MultiArray(data=sorted_array)
        self.publisher_.publish(sorted_msg)
        self.get_logger().info(f'Sorted array: {sorted_msg.data}')


def main(args=None):
    rclpy.init(args=args)
    array_sorter = ArraySorterNode()
    rclpy.spin(array_sorter)
    array_sorter.destroy_node
    rclpy.shutdown()

if __name__ == "__main__":
    main()
