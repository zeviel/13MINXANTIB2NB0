import AminoLab
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_STEEL_BLUE + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoantibanbo", font="smslant"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
print("""[1] On AntiBan
[2] Off AntiBan""")
select = input("Select >> ")

content = open("antiban_text.txt").read()

if select == "1":
    try:
        client.edit_profile(ndc_Id=ndc_Id, content=content)
        print("AntiBan Onned!")
    except Exception as e:
        print(e)

elif select == "2":
    try:
        content = "github.com/LilZevi"
        client.edit_profile(ndc_Id=ndc_Id, content=content)
        print("AntiBan Offed")
    except Exception as e:
        print(e)
