// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../../cpp/simulator/inc/inc/NBodySimulator.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

void export_nbodysimulator(py::module &m) {

  py::class_<simulator::NBodySimulator>(m, "NBodySimulator")
      .def(py::init<>())
      .def("setName",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::setName),
           py::arg("name"))
      .def("getName", py::overload_cast<>(&simulator::NBodySimulator::getName,
                                          py::const_));
}
