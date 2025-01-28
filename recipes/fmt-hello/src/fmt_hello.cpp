#include "fmt_hello.h"

#include <iostream>
#include <fmt/core.h>

namespace consumer {

void print_fmt_version() {
    std::cout << "fmt version: " << FMT_VERSION << std::endl;
}

}
