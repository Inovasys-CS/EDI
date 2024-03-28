Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select * From Win32_ShadowCopy")
    For Each objItem in colItems
	errResult = objItem.Delete_
    Next
wscript.Quit(errResult)