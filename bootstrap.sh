#!/bin/bash

set -ex

CONAN_CONF_VERBOSE="-c tools.build:verbosity=verbose -c tools.compilation:verbosity=verbose"
CONAN_CONF_SYS_PKG="-c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True"

#pushd recipes/libfmt/
#conan create all/ --version=system $CONAN_CONF_VERBOSE $CONAN_CONF_SYS_PKG
#popd

pushd recipes/fmt-hello/
conan create ./ $CONAN_CONF_VERBOSE $CONAN_CONF_SYS_PKG
popd

pushd recipes/fmt-app/
conan create ./ $CONAN_CONF_VERBOSE $CONAN_CONF_SYS_PKG
popd
