// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../../cpp/simulator/inc/inc/Vector2D.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>

namespace py = pybind11;

void export_Vector2D(py::module &m) {

  py::class_<simulator::Vector2D>(m, "Vector2D")
      .def(py::init<double, double>())
      .def_readwrite("x", &simulator::Vector2D::m_x)
      .def_readwrite("y", &simulator::Vector2D::m_y);
}
