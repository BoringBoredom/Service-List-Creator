Script to convert a service list into a registry file


example:

service1	description1
service2	description2
service3	description3

will convert into

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service1]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service2]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\service3]
"Start"=dword:00000004
