// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../../cpp/simulator/inc/inc/NBodySimulator.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

void export_NBodySimulator(py::module &m) {

  py::class_<simulator::NBodySimulator>(m, "NBodySimulator")
      .def(py::init<>())
      .def("addBody",
           py::overload_cast<std::string const &, double,
                             simulator::Vector2D const &,
                             simulator::Vector2D const &>(
               &simulator::NBodySimulator::addBody),
           py::arg("name"), py::arg("mass"), py::arg("position"),
           py::arg("velocity"))
      .def("removeBody",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::removeBody),
           py::arg("name"))
      .def("numberOfBodies",
           py::overload_cast<>(&simulator::NBodySimulator::numberOfBodies,
                               py::const_))
      .def("bodyNames", py::overload_cast<>(
                            &simulator::NBodySimulator::bodyNames, py::const_))
      .def("mass",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::mass, py::const_),
           py::arg("bodyName"))
      .def("initialPosition",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::initialPosition, py::const_),
           py::arg("bodyName"))
      .def("initialVelocity",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::initialVelocity, py::const_),
           py::arg("bodyName"));
}
