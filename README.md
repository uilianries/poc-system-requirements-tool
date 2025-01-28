## POC: System requirements as tool requirements only

This POC is a study over the Conan issue https://github.com/conan-io/conan/issues/16625

### Description

This POC validates the scenario when consuming a package that wraps a system requirement, and the consumer does not need to have the system requirement installed.

It's not possible to add visibility/visible directly via [system_requirements](https://docs.conan.io/2/reference/tools/system/package_manager.html), but we can manage
it via [requirements](https://docs.conan.io/2/reference/conanfile/methods/requirements.html#visible).


### How to build and validate on Linux this POC

./boostrap.sh

It will package fmtlib-dev in Ubuntu to the package libfmt/system
Then, will create the package fmt-hell that prints a string using fmt
Finally, fmt-app consumes fmt-hello and executes its method


### Build logs and validation

- [build_private_header.log](build_private_header.log): The fmt-hello consumes only fmt headers to print FMT_VERSION. Visibility is private. fmt-app does not fail to link/build.
- [build_private_lib.log](build_private_lib.log): The fmt-hello consumes fmt headers and fmt library to print formatted string. Visibility is private. fmt-app does fail to link/build due missing symbols (expected).
- [build-consumer-sys-reqs.log](build-consumer-sys-reqs.log): The fmt-hello consumes fmt headers and fmt library to print formatted string. Visibility is public. fmt-app does not fail to link/build.
