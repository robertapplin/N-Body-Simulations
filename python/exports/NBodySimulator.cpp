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
      .def("removeBody",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::removeBody),
           py::arg("name"))
      .def("addBody",
           py::overload_cast<std::string const &, double,
                             simulator::Vector2D const &,
                             simulator::Vector2D const &>(
               &simulator::NBodySimulator::addBody),
           py::arg("name"), py::arg("mass"), py::arg("position"),
           py::arg("velocity"))
      .def("setTimeStep",
           py::overload_cast<double>(&simulator::NBodySimulator::setTimeStep),
           py::arg("timeStep"))
      .def("timeStep", py::overload_cast<>(&simulator::NBodySimulator::timeStep,
                                           py::const_))
      .def("setDuration",
           py::overload_cast<double>(&simulator::NBodySimulator::setDuration),
           py::arg("duration"))
      .def("duration", py::overload_cast<>(&simulator::NBodySimulator::duration,
                                           py::const_))
      .def("numberOfBodies",
           py::overload_cast<>(&simulator::NBodySimulator::numberOfBodies,
                               py::const_))
      .def("bodyNames", py::overload_cast<>(
                            &simulator::NBodySimulator::bodyNames, py::const_))
      .def("setMass",
           py::overload_cast<std::string const &, double>(
               &simulator::NBodySimulator::setMass),
           py::arg("bodyName"), py::arg("mass"))
      .def("mass",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::mass, py::const_),
           py::arg("bodyName"))
      .def("setXPosition",
           py::overload_cast<std::string const &, double>(
               &simulator::NBodySimulator::setXPosition),
           py::arg("bodyName"), py::arg("x"))
      .def("setYPosition",
           py::overload_cast<std::string const &, double>(
               &simulator::NBodySimulator::setYPosition),
           py::arg("bodyName"), py::arg("y"))
      .def("setXVelocity",
           py::overload_cast<std::string const &, double>(
               &simulator::NBodySimulator::setXVelocity),
           py::arg("bodyName"), py::arg("vx"))
      .def("setYVelocity",
           py::overload_cast<std::string const &, double>(
               &simulator::NBodySimulator::setYVelocity),
           py::arg("bodyName"), py::arg("vy"))
      .def("initialPosition",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::initialPosition, py::const_),
           py::arg("bodyName"))
      .def("initialVelocity",
           py::overload_cast<std::string const &>(
               &simulator::NBodySimulator::initialVelocity, py::const_),
           py::arg("bodyName"))
      .def("runSimulation",
           py::overload_cast<>(&simulator::NBodySimulator::runSimulation));
}
