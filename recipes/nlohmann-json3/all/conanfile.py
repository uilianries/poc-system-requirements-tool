from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.system import package_manager
from conan.tools.gnu import PkgConfig

required_conan_version = ">=2.0.9"


class LibUDEVConan(ConanFile):
    name = "nlohmann-json3"
    version = "system"
    description = "JSON for Modern C++"
    topics = ("json", "json-parser", "header-only")
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://nlohmann.github.io/json/"
    license = "MIT"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        pass

    def validate(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration(f"{self.ref.name} system package is only supported on Linux.")

    def package_id(self):
        self.info.clear()

    def system_requirements(self):
        dnf = package_manager.Dnf(self)
        dnf.install(["json-devel"], update=True, check=True)

        yum = package_manager.Yum(self)
        yum.install(["json-devel"], update=True, check=True)

        apt = package_manager.Apt(self)
        apt.install(["nlohmann-json3-dev"], update=True, check=True)

        pacman = package_manager.PacMan(self)
        pacman.install(["nlohmann-json"], update=True, check=True)

        zypper = package_manager.Zypper(self)
        zypper.install(["nlohmann_json"], update=True, check=True)

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        pkg_config = PkgConfig(self, "nlohmann_json")
        pkg_config.fill_cpp_info(self.cpp_info)
        self.cpp_info.set_property("system_package_version", str(pkg_config.version))
