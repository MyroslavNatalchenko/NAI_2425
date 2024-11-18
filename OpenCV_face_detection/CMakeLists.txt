cmake_minimum_required(VERSION 3.29)
project(Mirya_project)

set(CMAKE_CXX_STANDARD 20)
find_package(OpenCV REQUIRED)

add_executable(Mirya_project main.cpp)

target_link_libraries(Mirya_project ${OpenCV_LIBS})
