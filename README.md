Serviwin (https://www.nirsoft.net/utils/serviwin.html) supports multiple selection of services and drivers and allows the user to "Copy Selected Items" (next to the "Refresh" button at the top) or by pressing CTRL + C. The content can be pasted into a file called "services.txt". This script alphabetically sorts and converts the resulting list into a registry file (all entries set to *disabled*). Optionally, services can be temporarily filtered out from the final registry file with a "-" prefix. The unsorted "services.txt" will be renamed to "services_unsorted.txt" and the sorted output will be saved as "services.txt". Move "services.txt" to the folder containing this script and run it.

example:

>SERVICE4 description4, additional description4 etc.  
>service2 description2, additional description2 etc.  
>service3 description3, additional description3 etc.  
>-service1 description1, additional description1 etc.  

will convert into

>-service1 description1, additional description1 etc.  
>service2 description2, additional description2 etc.  
>service3 description3, additional description3 etc.  
>SERVICE4 description4, additional description4 etc.  

as .txt file and

>Windows Registry Editor Version 5.00
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service2]  
>"Start"=dword:00000004
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service3]  
>"Start"=dword:00000004
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\SERVICE4]  
>"Start"=dword:00000004

as .reg file.
