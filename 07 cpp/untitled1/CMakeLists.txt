cmake_minimum_required(VERSION 3.29)
project(untitled1)
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(CMAKE_CXX_STANDARD 20)

add_executable(untitled1 main.cpp)

target_link_libraries( untitled1 ${OpenCV_LIBS} )
