# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import nox

HERE = os.path.abspath(os.path.dirname(__file__))

# -- REQUIRES: nox >= 2023.04.22
# SEE: https://nox.thea.codes/en/stable/index.html
USE_PYTHON_VERSIONS = os.environ.get("NOXFILE_PYTHON_VERSIONS", "").split()
if not USE_PYTHON_VERSIONS:
    with open(os.path.join(HERE, ".python-versions-used"), "r") as file:
        USE_PYTHON_VERSIONS = [x.strip() for x in file]


install_commands = (("pip", "install", "."), ("pip", "install", "-e", "."))


def install_packages(session, package_a, package_b, command_a, command_b):
    env = {**os.environ, "PIP_CONSTRAINT": f"{HERE}/constraints.txt"}
    session.install("--upgrade", "pip", env=env)
    session.chdir(package_a)
    session.run("rm", "-rf", "dist", "build", "*.egg-info")
    session.run(*command_a, env=env)
    session.chdir(HERE)
    session.chdir(package_b)
    session.run("rm", "-rf", "dist", "build", "*.egg-info")
    session.run(*command_b, env=env)
    session.chdir(HERE)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize("command_a", install_commands)
@nox.parametrize("command_b", install_commands)
def session_pkgutil(session, command_a, command_b):
    install_packages(session, "pkgutil\\pkg_a\\", "pkgutil\\pkg_b\\", command_a, command_b)
    session.run("python", "verify_packages.py")
