#include <iostream>

#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    const nlohmann::json data = {
        {"pi", 3.141},
    };

#if JSON_USE_IMPLICIT_CONVERSIONS
    float f = data["pi"];
#else
    auto f = data["pi"].get<float>();
#endif
    std::cout << data.dump(4) << "\n";
    return 0;
}
