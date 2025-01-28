#include "json_consumer.h"

#include <nlohmann/json.hpp>
#include <iostream>

namespace consumer {

void show_pi() {
    using json = nlohmann::json;

    const nlohmann::json data = {
        {"pi", 3.141},
    };

    #if JSON_USE_IMPLICIT_CONVERSIONS
        float f = data["pi"];
    #else
        auto f = data["pi"].get<float>();
    #endif
    std::cout << data.dump(4) << "\n";
}

}
