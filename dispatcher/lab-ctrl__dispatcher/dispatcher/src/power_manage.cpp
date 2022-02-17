// std headers
#include <Windows.h>
#include <reason.h>
#include <winreg.h>
#include <iostream>

// user-def headers
#include "power_manage.hpp"
#include "utils.hpp"

// std lib linkages
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "advapi32.lib")


// functions
namespace lab_ctrl {
    /*
    *  ShutsDown the child dispatcher is executed.
    *  ** Forcibly closes all the running processes
    *  ** Displays a warning for user and waits for 30 seconds
    */
    BOOL shutdown_child(BOOL restart)
    {
        HANDLE hToken;      // token handler for the cureent proc token
        
        // Retrieve Token for Current Proc from the OS
        if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken))
        {
            lab_ctrl::LogErrorCode("Token Retrieval failed.");
            return FALSE;
        }

        // Adjust the privilege for current token
        lab_ctrl::AdjustPrivilege(hToken, SE_SHUTDOWN_NAME, 1);

        auto status = GetLastError();

        if (status != ERROR_SUCCESS)
        {
            lab_ctrl::LogErrorCode("Failed to escalate.");
            return FALSE;
        }

        // Shutdown the system and force all applications to close. 
        status = InitiateSystemShutdown(
            // Str-Ptr represeting the machine to shutdown, NULL - Local Machine
            NULL,
            
            // Str-Ptr for the message to be displayed to the logged on user
            NULL,
            
            // Time to display the disclaimer for shutdown in seconds
            30,
            
            // Whether to forcibly close/end running apps
            TRUE,
            
            // Whther to restart the system after shutdown
            restart
        );

        if (status)
        {
            
            /* shutdown initiated
            *  ------------------
            *  A success(<0) code doesn't mean system will be shutdown for sure as many
            *  factors could terminate the shutdown process.
            *  refer: https://docs.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-initiatesystemshutdownexa#remarks
            */

            return TRUE;
        }
        else
        {
            // something went wrong
            lab_ctrl::LogErrorCode("InitiateSystemShutdown failed.");
            return FALSE;
        }

    }
}