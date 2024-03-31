#include "pch.h"
#include <windows.h>
#include <wininet.h>
#pragma comment(lib, "wininet.lib")

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

// Adjusted to use wide characters
extern "C" __declspec(dllexport) void CALLBACK SendHttpGetRequest(HWND hwnd, HINSTANCE hinst, LPWSTR lpszCmdLine, int nCmdShow) {
    HINTERNET hInternet, hConnect;
    DWORD bytesRead;
    wchar_t buffer[2048]; // Changed to wchar_t

    // Initialize WinINet API with a wide string
    hInternet = InternetOpen(L"HttpDllRequest", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    if (hInternet == NULL) return;

    // Make a connection to ipinfo.io with a wide string URL
    hConnect = InternetOpenUrl(hInternet, L"https://api.ipify.org", NULL, 0, INTERNET_FLAG_RELOAD, 0);
    if (hConnect == NULL) {
        InternetCloseHandle(hInternet);
        return;
    }

    // Read the response into buffer
    if (InternetReadFile(hConnect, buffer, sizeof(buffer), &bytesRead)) {
        // Null-terminate the wide string
        if (bytesRead < sizeof(buffer) / sizeof(wchar_t)) {
            buffer[bytesRead / sizeof(wchar_t)] = 0;
        }
        else {
            buffer[(sizeof(buffer) / sizeof(wchar_t)) - 1] = 0;
        }
        MessageBox(NULL, buffer, L"HTTP GET Response", MB_OK); // Use wide string literals
    }

    InternetCloseHandle(hConnect);
    InternetCloseHandle(hInternet);
}
