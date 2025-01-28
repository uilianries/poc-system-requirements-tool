from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.system import package_manager
from conan.tools.gnu import PkgConfig

required_conan_version = ">=2.0.9"


class formatterConan(ConanFile):
    name = "libfmt"
    version = "system"
    description = "fast type-safe C++ formatting library"
    topics = ("string", "formatter")
    homepage = "https://fmt.dev/"
    license = "MIT"
    package_type = "shared-library"
    settings = "os", "arch"

    def layout(self):
        pass

    def validate(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration(f"{self.ref.name} system package is only supported on Linux.")

    def package_id(self):
        self.info.clear()

    def system_requirements(self):
        dnf = package_manager.Dnf(self)
        dnf.install(["fmt-devel"], update=True, check=True)

        yum = package_manager.Yum(self)
        yum.install(["fmt-devel"], update=True, check=True)

        apt = package_manager.Apt(self)
        apt.install(["libfmt-dev"], update=True, check=True)

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        pkg_config = PkgConfig(self, "fmt")
        pkg_config.fill_cpp_info(self.cpp_info)
        self.cpp_info.set_property("system_package_version", str(pkg_config.version))
