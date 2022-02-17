#pragma once

#include <Windows.h>

namespace lab_ctrl {
	class Nurse
	{
	public:
		// constructor
		Nurse();
		// empty destructor
		~Nurse();
		// get total RAM size in MB
		DWORDLONG getTotalPhysicalMemory();
		// get free RAM size in MB
		DWORDLONG getAvailableMemory();
		// get CPU load percentage
		float getCPULoad();
		// get WindowsOS info
		DWORDLONG getOSStat();

	private:
		// global var to minimize #ofQueries to the OS API
		MEMORYSTATUSEX stat;
		// utility functions
		unsigned long long FileTimeToInt64(const FILETIME& ft);
		// calculate cpu load percentage from system times
		float CalculateCPULoad(unsigned long long idleTicks, unsigned long long totalTicks);
		// to init the this->stat
		void GetStats();
	};
}
