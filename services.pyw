service_list = []

with open("services.txt", "r") as f:
    for line in f:
        service_list.append(line.split()[0])

with open("services.reg", "w") as f:
    f.write("Windows Registry Editor Version 5.00")
    for service in service_list:
        f.write("\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\\" + service + "]\n" + "\"Start\"=dword:00000004")
