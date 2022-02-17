#pragma once

namespace lab_ctrl {
    /* 
    * AdjustPrivilege()
    * -----------------
    * Adjust the Privilege of the current process 
    * by manipuating the token. Belongs to Windows OSes.
    * 
    * Params:
    *   hToken: `HANDLE` type token-handler of the process that needs escalation
    *   lpszPrivilege: long pointer to c-string that describes the privilege.
    *                  This must be one of https://docs.microsoft.com/en-us/windows/win32/secauthz/authorization-constants
    *   bEnablePrivilege: Booloean swith to whether enable/disable the specified privilege
    *                     1 - Enble and 0 - Disable
    */
    BOOL AdjustPrivilege(
        HANDLE hToken,          
        LPCTSTR lpszPrivilege,  
        BOOL bEnablePrivilege   
    );


    /*
    * LogErrorCode()
    * --------------
    * Logs the last error code to std::cerr with a specified message if DEBUG is defined
    * 
    * Params:
    *   message: string representing message to be logged along with the error code
    */
    void LogErrorCode(std::string message);


    /*
    * Log()
    * --------------
    * Logs the  a specified message
    *
    * Params:
    *   message: string representing message to be logged 
    */
    void Log(std::string message);
    void Log(float message);
    void Log(DWORDLONG message);
}
