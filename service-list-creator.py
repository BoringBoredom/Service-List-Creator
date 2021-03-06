import os, requests

current_version = 0.10

try:
    r = requests.get("https://api.github.com/repos/BoringBoredom/Service-List-Creator/releases/latest")
    new_version = float(r.json()["tag_name"])
    if new_version > current_version:
        with open("NEW VERSION AVAILABLE.txt", "w") as d:
            d.write(f"{new_version} available at https://github.com/BoringBoredom/Service-List-Creator/releases/latest. Your current version is {current_version}")
except:
    pass

service_list = []
full_list = []

with open("services.txt", "r") as f:
    for line in f:
        try:
            service_list.append(line.split()[0])
            if "\n" not in line:
                line = line + "\n"
            full_list.append(line)
        except IndexError:
            pass

sorted_service_list = sorted(service_list, key= lambda x: (x.strip("-").casefold()))
sorted_full_list = sorted(full_list, key= lambda x: (x.strip("-").casefold()))

os.rename("services.txt", "services_unsorted.txt")

with open("services.txt", "w") as f:
    for entry in sorted_full_list:
        f.write(entry)

with open("services.reg", "w") as f:
    f.write("Windows Registry Editor Version 5.00")
    for service in sorted_service_list:
        if "-" not in service:
            f.write("\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\\" + service + "]\n\"Start\"=dword:00000004")
