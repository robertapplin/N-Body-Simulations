import os
import subprocess
import sys
import sysconfig

from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    """A class used as to create an extension module for setup."""

    def __init__(self, name: str, source_directory: str):
        """Initialize the CMake extension."""
        Extension.__init__(self, name, sources=[])
        self.source_directory = source_directory


class CMakeBuild(build_ext):
    """A class used to build the project using CMake."""

    def build_extension(self, extension: CMakeExtension) -> None:
        """Generates and builds the project using CMake."""
        extension_directory = self._get_extension_directory(extension)
        site_package_directory = sysconfig.get_paths()["purelib"]
        pybind11_directory = os.path.join(site_package_directory, "pybind11", "share", "cmake", "pybind11")

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE={extension_directory}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DPYTHON_LIBRARY_DIR={site_package_directory}",
            f"-Dpybind11_DIR={pybind11_directory}"
        ]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(["cmake", extension.source_directory, "-A", "x64"] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(["cmake", "--build", ".", "--config", "Release"], cwd=self.build_temp)

    def _get_extension_directory(self, extension: CMakeExtension) -> str:
        """Generates and builds the project using CMake."""
        extension_directory = os.path.abspath(os.path.dirname(self.get_ext_fullpath(extension.name)))
        if not extension_directory.endswith(os.path.sep):
            extension_directory += os.path.sep
        return extension_directory


setup(
    name="n_body_simulations",
    version="1.0.1",
    author="Robert Applin",
    author_email="robertgjapplin@gmail.com",
    description="A QWidget used for simulating a gravitational system of N bodies in two dimensions.",
    ext_modules=[CMakeExtension("NBodySimulations", os.path.dirname(os.path.realpath(__file__)))],
    cmdclass={"build_ext": CMakeBuild},
    packages=find_packages(),
    zip_safe=False,
    install_requires=["matplotlib", "qtawesome"],
    extras_require={"test": ["pytest", "pytest-mock", "pytest-qt==3.3.0"]},
    python_requires=">=3.8"
)
