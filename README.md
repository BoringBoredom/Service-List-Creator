This scripts sorts and converts a service list into a registry file. The service list should be named services.txt and contain one service and optional descriptions per line. Optionally, services can be filtered out from the final registry file with a "-" prefix. The unsorted services.txt will be renamed to services_unsorted.txt and the sorted output will be saved as services.txt. The amount of whitespaces between a service and its description is irrelevant.

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

Place the script into the same folder as services.txt and run it.
