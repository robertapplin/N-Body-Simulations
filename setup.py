import os
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


class CMakeExtension(Extension):

    def __init__(self, name: str, source_directory: str):
        Extension.__init__(self, name, sources=[])
        self.source_directory = source_directory


class CMakeBuild(build_ext):

    def build_extension(self, extension: CMakeExtension):
        extension_directory = os.path.abspath(os.path.dirname(self.get_ext_fullpath(extension.name)))

        # required for auto-detection & inclusion of auxiliary "native" libs
        if not extension_directory.endswith(os.path.sep):
            extension_directory += os.path.sep

        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        config = "Debug" if debug else "Release"

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extension_directory}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={config}",  # not used on MSVC, but no harm
        ]
        build_args = []
        # Adding CMake arguments set as environment variable
        # (needed e.g. to build for ARM OSx on conda-forge)
        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        # In this example, we pass in the version to C++. You might not need to.
        cmake_args += [f"-DEXAMPLE_VERSION_INFO={self.distribution.get_version()}"]

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator:
                try:
                    import ninja  # noqa: F401

                    cmake_args += ["-GNinja"]
                except ImportError:
                    pass

        else:

            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward compatibility
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{config.upper()}={extension_directory}"
                ]
                build_args += ["--config", config]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(
            ["cmake", extension.source_directory] + cmake_args, cwd=self.build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=self.build_temp
        )
        # subprocess.check_call(
        #     ["cmake", "--install", "."], cwd=self.build_temp
        # )


setup(
    name="n_body_simulations",
    version="1.0.1",
    author="Robert Applin",
    author_email="robertgjapplin@gmail.com",
    description="A QWidget used for simulating a gravitational system of N bodies in two dimensions.",
    ext_modules=[CMakeExtension("n_body_simulations", os.path.dirname(os.path.realpath(__file__)))],
    cmdclass={"build_ext": CMakeBuild},
    packages=["n_body_simulations.plotting", "n_body_simulations.qt", "n_body_simulations.qt.ui",
              "n_body_simulations.xml"],
    install_requires=["matplotlib", "pybind11", "pyside2", "pyqt5", "qtawesome"],
    extras_require={"test": ["pytest", "pytest-mock", "pytest-qt==3.3.0"]},
    python_requires=">=3.8",
)
