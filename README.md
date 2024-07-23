# `haj_cv3_sorter` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/sze-info/haj_cv3_sorter
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select haj_cv3_sorter --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 run haj_cv3_sorter array_sorter
```

``` r
ros2 topic pub /input_array std_msgs/msg/Float32MultiArray "{'data': [3.0, 1.0, 256.1, -24.5, 4.0, 1.5, 13.5, 9.6]}"
```


## Graph

``` mermaid
graph LR;

A[ /input_array<br/>std_msgs/msg/Float32MultiArray]:::light --> B([ /array_sorter]):::red
B --> C[ /sorted_array<br/>std_msgs/msg/Float32MultiArray]:::light 

classDef light fill:#34aec5,stroke:#152742,stroke-width:2px,color:#152742  
classDef dark fill:#152742,stroke:#34aec5,stroke-width:2px,color:#34aec5
classDef white fill:#ffffff,stroke:#152742,stroke-width:2px,color:#152742
classDef red fill:#ef4638,stroke:#152742,stroke-width:2px,color:#fff
```