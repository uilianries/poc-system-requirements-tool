cmake_minimum_required(VERSION 3.15)
project(fmt-app CXX)

find_package(fmt-hello REQUIRED CONFIG)

add_executable(fmt-app src/main.cpp)
target_link_libraries(fmt-app PRIVATE fmt-hello::fmt-hello)


install(TARGETS fmt-app DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
