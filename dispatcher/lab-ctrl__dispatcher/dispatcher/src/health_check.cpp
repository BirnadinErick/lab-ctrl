// headers linkage
#include <Windows.h>

#include "health_check.h"

// to convert bytes to MB
#define DividantForMB 1048576


// an object to get state check of a child
namespace lab_ctrl {

	Nurse::Nurse()
	{
		// initiate the stats
		this->GetStats();
	}

	Nurse::~Nurse()
	{
		// TODO: deallocate the neccessary objects
	}
	DWORDLONG Nurse::getTotalPhysicalMemory()
	{
		DWORDLONG RAMSizeInMB;
		// get the RAM from `stat` attr
		RAMSizeInMB = this->stat.ullTotalPhys / DividantForMB;
		return RAMSizeInMB;
	}
	DWORDLONG Nurse::getAvailableMemory()
	{
		DWORDLONG UsedRAMSizeInMB;
		// get the RAM from `stat` attr
		UsedRAMSizeInMB = this->stat.ullAvailPhys / DividantForMB;
		return UsedRAMSizeInMB;
	}
	float Nurse::getCPULoad()
	{
		// time vars to store the time
		FILETIME idleTime, kernelTime, userTime;
		// get the system time and calc
		// sippet from: https://stackoverflow.com/questions/23143693/retrieving-cpu-load-percent-total-in-windows-with-c
		return GetSystemTimes(&idleTime, &kernelTime, &userTime) 
			? this->CalculateCPULoad(FileTimeToInt64(idleTime), this->FileTimeToInt64(kernelTime) + FileTimeToInt64(userTime)) 
			: -1.0f;
		
	}
	DWORDLONG Nurse::getOSStat()
	{
		return DWORDLONG();
	}
	void Nurse::GetStats()
	{
		this->stat.dwLength = sizeof(MEMORYSTATUSEX);
		GlobalMemoryStatusEx(&this->stat);
	}
	float Nurse::CalculateCPULoad(unsigned long long idleTicks, unsigned long long totalTicks)
	{
		static unsigned long long _previousTotalTicks = 0;
		static unsigned long long _previousIdleTicks = 0;

		unsigned long long totalTicksSinceLastTime = totalTicks - _previousTotalTicks;
		unsigned long long idleTicksSinceLastTime = idleTicks - _previousIdleTicks;


		float ret = 1.0f - ((totalTicksSinceLastTime > 0) ? ((float)idleTicksSinceLastTime) / totalTicksSinceLastTime : 0);

		_previousTotalTicks = totalTicks;
		_previousIdleTicks = idleTicks;
		return ret;
	}
	unsigned long long Nurse::FileTimeToInt64(const FILETIME& ft)
	{
		return (((unsigned long long)(ft.dwHighDateTime)) << 32) | ((unsigned long long)ft.dwLowDateTime);
	}

}
