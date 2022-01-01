import pybind11
import os
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    """A class used as to create an extension module for setup."""

    def __init__(self, name: str, source_directory: str):
        """Initialize the CMake extension."""
        Extension.__init__(self, name, sources=[])
        self.source_directory = source_directory


class CMakeBuild(build_ext):
    """A class used to build the project using CMake."""

    def build_extension(self, extension: CMakeExtension):
        """Generates and builds the project using CMake."""
        extension_directory = self._get_extension_directory(extension)

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extension_directory}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_PREFIX_PATH={pybind11.__path__}"
        ]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(["cmake", extension.source_directory] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(["cmake", "--build", ".", "--config", "Release"], cwd=self.build_temp)
        subprocess.check_call(["cmake", "--install", "."], cwd=self.build_temp)

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
    ext_modules=[CMakeExtension("n_body_simulations", os.path.dirname(os.path.realpath(__file__)))],
    cmdclass={"build_ext": CMakeBuild},
    packages=["n_body_simulations.plotting", "n_body_simulations.qt", "n_body_simulations.qt.ui",
              "n_body_simulations.xml_r"],
    install_requires=["matplotlib", "pybind11", "pyside2", "pyqt5", "qtawesome"],
    extras_require={"test": ["pytest", "pytest-mock", "pytest-qt==3.3.0"]},
    python_requires=">=3.8"
)
