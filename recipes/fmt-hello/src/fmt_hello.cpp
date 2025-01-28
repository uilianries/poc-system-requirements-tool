#include "fmt_hello.h"

#include <iostream>
#include <fmt/core.h>

namespace consumer {

void print_fmt_version() {
    fmt::print("Hello, world!\n");
    std::cout << "fmt version: " << FMT_VERSION << std::endl;

}

}
