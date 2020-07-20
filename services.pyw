import os

full_list = []
service_list = []

with open("services.txt", "r") as f:
    for line in f:
        full_list.append(line)
        service_list.append(line.split()[0])

sorted_full_list = sorted(full_list, key=str.casefold)
sorted_service_list = sorted(service_list, key=str.casefold)

os.rename("services.txt", "services_unsorted.txt")

with open("services.txt", "w") as f:
    for entry in sorted_full_list:
        f.write(entry)

with open("services.reg", "w") as f:
    f.write("Windows Registry Editor Version 5.00")
    for service in sorted_service_list:
        f.write("\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\\" + service + "]\n" + "\"Start\"=dword:00000004")
