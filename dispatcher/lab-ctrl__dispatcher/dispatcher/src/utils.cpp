// headers linkage
#include <windows.h>
#include <iostream>
#include <string>

#include "utils.hpp"

// std lib linkage
#pragma comment(lib, "advapi32.lib")

// utility functions

/*
     Referenced from MSDN docs, for more info refer the site
*/
namespace lab_ctrl {
    BOOL AdjustPrivilege(
        HANDLE hToken,              // access token handle
        LPCTSTR lpszPrivilege,      // name of privilege to enable/disable
        BOOL bEnablePrivilege       // to enable or disable privilege
    )
    {

        TOKEN_PRIVILEGES tp;
        LUID luid;

        if (!LookupPrivilegeValue(
            NULL,                   // lookup privilege on local system
            lpszPrivilege,          // privilege to lookup 
            &luid))                 // receives LUID of privilege
        {
            lab_ctrl::LogErrorCode("LookupPrivilegeValue failed.");
            return FALSE;
        }

        tp.PrivilegeCount = 1;
        tp.Privileges[0].Luid = luid;

        if (bEnablePrivilege)
        {
            tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED; // set the privilege to be enabled
        }
        else
        {
            tp.Privileges[0].Attributes = 0;                    // or to be diabled
        }
        
        // Enable/Disable the privilege specified
        if (!AdjustTokenPrivileges(
            hToken,
            FALSE,
            &tp,
            sizeof(TOKEN_PRIVILEGES),
            (PTOKEN_PRIVILEGES)NULL,
            (PDWORD)NULL))
        {
            lab_ctrl::LogErrorCode("AdjustTokenPrivileges failed.");
            return FALSE;
        }

        // Check for error and throw it
        if (GetLastError() == ERROR_NOT_ALL_ASSIGNED)
        {
            lab_ctrl::LogErrorCode("The token does not have the specified privilege.");
            return FALSE;
        }

        return TRUE; // indicate that privileage has been succesfully escalleted
    }

    void LogErrorCode(std::string message)
    {
#ifdef DEBUG
        std::cerr << message << " [Error Code:" << GetLastError() << "]" << std::endl;
#endif
        return;
    }

    void Log(std::string message) {
        std::cout << message << std::endl;
        return;
    }

    void Log(float message) {
        std::cout << message << std::endl;
        return;
    }

    void Log(DWORDLONG message) {
        std::cout << message << std::endl;
        return;
    }
}