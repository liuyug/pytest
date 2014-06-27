
#include <Python.h>

static PyObject * spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;
    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}

static PyObject * spam_add(PyObject *self, PyObject *args)
{
    int num1, num2;
    if (!PyArg_ParseTuple(args, "ii", &num1, &num2))
        return NULL;
    return Py_BuildValue("ii", num1 + num2, num1 - num2);
}

static PyMethodDef spam_methods[] = {
    {"system", spam_system, METH_VARARGS, "Execute a shell command."},
    {"add", spam_add, METH_VARARGS, "add."},
    {NULL, NULL, 0, NULL},
};

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initspam(void)
{
    Py_InitModule3("spam", spam_methods, "spam module");
}
#else
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam", "spam module", -1, spam_methods,
};

PyMODINIT_FUNC PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}

#endif
