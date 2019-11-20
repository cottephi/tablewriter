import os
to_return = ""
with open("setup.py","r") as ifile:
  lines = ifile.readlines()
  for i in range(len(lines)):
    if "version" in lines[i]:
      version = int(lines[i].split("=")[-1].split(".")[-1].replace("\",\n",""))
      version2 = version + 1
      lines[i] = lines[i].replace(str(version)+"\",\n", str(version2)+"\",\n")
      to_return = lines[i].replace(" ","")
      to_return = to_return.replace("\"","")
      to_return = to_return.replace("\n","")
      to_return = to_return.replace("version","")
      to_return = to_return.replace("=","")
      to_return = to_return.replace(",","")
with open("setup.py","w") as ofile:
  for line in lines:
    ofile.write(line)
print(to_return)
