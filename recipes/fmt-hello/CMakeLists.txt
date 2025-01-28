cmake_minimum_required(VERSION 3.15)
project(fmt_hello CXX)

find_package(fmt REQUIRED)

add_library(fmt_hello src/fmt_hello.cpp)
target_link_libraries(fmt_hello PRIVATE fmt::fmt)


install(TARGETS fmt_hello DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

install(FILES src/fmt_hello.h DESTINATION include)
