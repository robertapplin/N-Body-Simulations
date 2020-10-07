// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include <pybind11/pybind11.h>

namespace py = pybind11;

void export_Vector2D(py::module &);
void export_NBodySimulator(py::module &);

namespace mcl {

PYBIND11_MODULE(NBodySimulations, m) {
  export_Vector2D(m);
  export_NBodySimulator(m);
}

} // namespace mcl
