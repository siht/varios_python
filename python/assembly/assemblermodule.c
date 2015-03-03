#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

static PyObject *
assembler_fdivide(PyObject *self, PyObject *args)
{
    const float a, b;
    float r = 0;
    if (!PyArg_ParseTuple(args, "ff", &a, &b))
        return NULL;
    __asm__ __volatile__(
    "fld %1;"
    "fld %2;"
    "fdivp;"
    "fstp %0;"
    : "=g" (r)
    : "g" (b), "g" (a)
    );
    return Py_BuildValue("f", r);
}

static PyMethodDef AssemblerMethods[] = {
    {"fdivide",  assembler_fdivide, METH_VARARGS, "division por ensamblador."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initassembler(void)
{
    (void) Py_InitModule("assembler", AssemblerMethods);
}
