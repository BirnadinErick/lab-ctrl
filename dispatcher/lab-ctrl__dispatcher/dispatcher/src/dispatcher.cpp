// headers linkage
#include <iostream>
#include <Windows.h>

#include "power_manage.hpp"
#include "utils.hpp"

using namespace lab_ctrl;

// Executable entry
int main(int argc, char** argv)
{
	Log("Lab-Ctrl Dispatcher");
	
	BOOL status = shutdown_child();

	if (status)
	{
		Log("Done!");
		return 0;
	}
	else
	{
		return 1;
	}
}