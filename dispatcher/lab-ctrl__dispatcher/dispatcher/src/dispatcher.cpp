// headers linkage
#include <iostream>
#include <Windows.h>
#include <stdlib.h>

#include "power_manage.hpp"
#include "utils.hpp"
#include "health_check.h"


// definitions of actions
#define SHUTDOWN 1
#define LOGOFF 2
#define RESTART 3
#define EXEC_CMD 4
#define HEALTH_CHECK 6

using namespace lab_ctrl;

// Executable entry
int main(int argc, char* argv[])
{
	int trigger = atoi(argv[1]);
	lab_ctrl::Nurse localNurse = lab_ctrl::Nurse();
	
	switch (trigger)
	{
	case SHUTDOWN:
		if (shutdown_child(FALSE))
		{
			Log("Shutting down...");
			exit(0);
		}
		else
		{
			exit(1);
		}
	case LOGOFF:
		Log("Logging off...");
		break;
	case RESTART:
		if (shutdown_child(TRUE))
		{
			Log("Restartig...");
			exit(0);
		}
		else
		{
			exit(1);
		}
	case EXEC_CMD:
		system(argv[2]);
		break;
	case HEALTH_CHECK:
		DWORDLONG RAMAvail, RAMTotal;
		float CPULoad;
		RAMAvail = localNurse.getAvailableMemory();
		RAMTotal = localNurse.getTotalPhysicalMemory();
		CPULoad = localNurse.getCPULoad() * 100;
		
		// test output
		/*std::cout << "Total RAM: "<< RAMTotal <<" MB" << std::endl;
		std::cout << "Avail RAM: "<< RAMAvail <<" MB" << std::endl;
		std::cout << "Current CPU Load: "<< CPULoad * 100 <<" %" << std::endl;*/
		
		// output the calculated values
		lab_ctrl::Log(RAMAvail);
		lab_ctrl::Log(RAMTotal);
		lab_ctrl::Log(CPULoad);
		break;
	default:
		break;
	}
}