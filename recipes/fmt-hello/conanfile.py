from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class json_consumerRecipe(ConanFile):
    name = "fmt-hello"
    version = "0.3.0"
    package_type = "library"
    settings = "os", "arch", "build_type", "compiler"
    exports_sources = "CMakeLists.txt", "src/*"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    implements = "auto_shared_fpic"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("libfmt/system", visible=False)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["fmt_hello"]
