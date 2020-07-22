This scripts sorts and converts a service list into a registry file. The service list should be named services.txt and contain one service and optional descriptions per line. The unsorted services.txt will be renamed into services_unsorted.txt and the sorted output will save into services.txt.

example:

>service2 description2, additional description2 etc.  
>service1 description1, additional description1 etc.  
>service3 description3, additional description3 etc.  

will convert into

>service1 description1, additional description1  
>service2 description2, additional description2  
>service3 description3, additional description3  

as .txt file and

>Windows Registry Editor Version 5.00
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service1]  
>"Start"=dword:00000004
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service2]  
>"Start"=dword:00000004
>
>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service3]  
>"Start"=dword:00000004

as .reg file.

Place the script into the same folder as services.txt and run it.
