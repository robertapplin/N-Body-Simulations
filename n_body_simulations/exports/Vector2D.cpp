// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Vector2D.h"

#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

void export_Vector2D(py::module &m) {

  py::class_<Simulator::Vector2D>(m, "Vector2D")
      .def(py::init<double, double>())
      .def_readwrite("x", &Simulator::Vector2D::m_x)
      .def_readwrite("y", &Simulator::Vector2D::m_y)
      .def("__eq__", &Simulator::Vector2D::operator==, py::is_operator())
      .def("magnitude",
           py::overload_cast<>(&Simulator::Vector2D::magnitude, py::const_));
}
