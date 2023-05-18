#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *obj)
{
	long int size;
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(obj, &str, &size);

	printf("  size: %li\n", size);
	printf("  string: %s\n", str);
	printf("  first %li bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

void print_python_list(PyObject *obj)
{
	long int size = PyList_Size(obj);
	int i;
	PyListObject *list = (PyListObject *)obj;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size; i++)

	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
