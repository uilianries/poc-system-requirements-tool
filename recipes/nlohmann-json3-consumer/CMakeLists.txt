cmake_minimum_required(VERSION 3.15)
project(json-consumer CXX)

find_package(nlohmann_json REQUIRED)

add_library(json-consumer-lib src/json_consumer.cpp)
target_link_libraries(json-consumer-lib PRIVATE nlohmann_json::nlohmann_json)

add_executable(json-consumer src/main.cpp)
target_link_libraries(json-consumer PRIVATE json-consumer-lib)
target_include_directories(json-consumer PRIVATE src)

install(TARGETS json-consumer json-consumer-lib DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

install(FILES src/json_consumer.h DESTINATION include)
