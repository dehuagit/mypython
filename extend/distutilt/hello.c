#include <Python.h>
#include <string.h>

/* module function*/
static PyObject * message(PyObject *self, PyObject *args)
{
  char *fromPython, result[1024];
  if (! PyArg_Parse(args, "(s)", &fromPython))    /*COnvert Python -> C */
    return NULL;
  else {
    strcpy(result, "Hello, ");  /*build up C string*/
    strcat(result, fromPython); /*add passed python string*/
    return Py_BuildValue("s", result);  /*convet c-> python*/
  }
}

/*Registration table*/
static PyMethodDef hello_methods[] = {
  {"message", message, METH_VARARGS, "func doc"},
  {NULL, NULL, 0, NULL}
};

/*moudce definition structuree*/
static struct PyModuleDef hellomodule = {
  PyModuleDef_HEAD_INIT,
  "hello",    /*name of moduel*/
  "mod doc",  /*nodule ducument, may be null*/
  -1,     /**size of perinterpreter modue sate, -1= global vars*/
  hello_methods /*link to method table*/
};

/*module initaializer*/
PyMODINIT_FUNC PyInit_hello()      /*called on first import */
{
  /*name matters if loaded dyncamce*/
/*return PyModule_Create(&hellomodule);*/
 return PyModule_Create(&hellomodule);
}


