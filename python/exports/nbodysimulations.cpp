// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include <pybind11/pybind11.h>

namespace py = pybind11;

void export_nbodysimulator(py::module &);

namespace mcl {

PYBIND11_MODULE(nbodysimulations, m) { export_nbodysimulator(m); }

} // namespace mcl
