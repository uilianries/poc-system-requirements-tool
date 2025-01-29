from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.system import package_manager


class json_consumerRecipe(ConanFile):
    name = "fmt-hello"
    version = "0.2.0"
    package_type = "library"
    settings = "os", "arch", "build_type", "compiler"
    exports_sources = "CMakeLists.txt", "src/*"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    implements = "auto_shared_fpic"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def _build_system_requirements(self):
        if self.settings.os == "Linux":
            dnf = package_manager.Dnf(self)
            dnf.install(["fmt-devel"], update=True, check=True)

            yum = package_manager.Yum(self)
            yum.install(["fmt-devel"], update=True, check=True)

            apt = package_manager.Apt(self)
            apt.install(["libfmt-dev"], update=True, check=True)

    def build(self):
        self._build_system_requirements()
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["fmt_hello"]
