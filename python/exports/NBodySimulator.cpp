// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

void export_NBodySimulator(py::module &m) {

  py::class_<Simulator::NBodySimulator>(m, "NBodySimulator")
      .def(py::init<>())
      .def("removeBody",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::removeBody),
           py::arg("name"))
      .def("addBody",
           py::overload_cast<std::string const &, double,
                             Simulator::Vector2D const &,
                             Simulator::Vector2D const &>(
               &Simulator::NBodySimulator::addBody),
           py::arg("name"), py::arg("mass"), py::arg("position"),
           py::arg("velocity"))
      .def("setTimeStep",
           py::overload_cast<double>(&Simulator::NBodySimulator::setTimeStep),
           py::arg("timeStep"))
      .def("timeStep", py::overload_cast<>(&Simulator::NBodySimulator::timeStep,
                                           py::const_))
      .def("setDuration",
           py::overload_cast<double>(&Simulator::NBodySimulator::setDuration),
           py::arg("duration"))
      .def("duration", py::overload_cast<>(&Simulator::NBodySimulator::duration,
                                           py::const_))
      .def("numberOfBodies",
           py::overload_cast<>(&Simulator::NBodySimulator::numberOfBodies,
                               py::const_))
      .def("bodyNames", py::overload_cast<>(
                            &Simulator::NBodySimulator::bodyNames, py::const_))
      .def("setName",
           py::overload_cast<std::string const &, std::string const &>(
               &Simulator::NBodySimulator::setName),
           py::arg("oldName"), py::arg("newName"))
      .def("setMass",
           py::overload_cast<std::string const &, double>(
               &Simulator::NBodySimulator::setMass),
           py::arg("bodyName"), py::arg("mass"))
      .def("mass",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::mass, py::const_),
           py::arg("bodyName"))
      .def("setXPosition",
           py::overload_cast<std::string const &, double>(
               &Simulator::NBodySimulator::setXPosition),
           py::arg("bodyName"), py::arg("x"))
      .def("setYPosition",
           py::overload_cast<std::string const &, double>(
               &Simulator::NBodySimulator::setYPosition),
           py::arg("bodyName"), py::arg("y"))
      .def("setXVelocity",
           py::overload_cast<std::string const &, double>(
               &Simulator::NBodySimulator::setXVelocity),
           py::arg("bodyName"), py::arg("vx"))
      .def("setYVelocity",
           py::overload_cast<std::string const &, double>(
               &Simulator::NBodySimulator::setYVelocity),
           py::arg("bodyName"), py::arg("vy"))
      .def("initialPosition",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::initialPosition, py::const_),
           py::arg("bodyName"))
      .def("initialVelocity",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::initialVelocity, py::const_),
           py::arg("bodyName"))
      .def("hasDataChanged",
           py::overload_cast<>(&Simulator::NBodySimulator::hasDataChanged,
                               py::const_))
      .def("runSimulation",
           py::overload_cast<>(&Simulator::NBodySimulator::runSimulation))
      .def("simulatedPositions",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::simulatedPositions, py::const_),
           py::arg("bodyName"))
      .def("simulatedVelocities",
           py::overload_cast<std::string const &>(
               &Simulator::NBodySimulator::simulatedVelocities, py::const_),
           py::arg("bodyName"));
}
