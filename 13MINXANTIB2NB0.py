import amino
print("""\033[38;5;45m
Script by deluvsushi
Github : https://github.com/deluvsushi
─╔╗─╔═══╗───────────────────────╔╗───╔╗──╔═══╗────╔╗──╔═══╗
╔╝║─║╔═╗║──────────────────────╔╝╚╗──║║──║╔═╗║────║║──║╔═╗║
╚╗║─╚╝╔╝║╔╗╔╗╔╗╔═╗─╔╗╔╗╔══╗╔═╗─╚╗╔╝╔╗║╚═╗╚╝╔╝║╔═╗─║╚═╗║║║║║
─║║─╔╗╚╗║║╚╝║─╣║╔╗╗╚╬╬╝║╔╗║║╔╗╗─║║──╣║╔╗║╔═╝╔╝║╔╗╗║╔╗║║║║║║
╔╝╚╗║╚═╝║║║║║║║║║║║╔╬╬╗║╔╗║║║║║─║╚╗║║║╚╝║║║╚═╗║║║║║╚╝║║╚═╝║
╚══╝╚═══╝╚╩╩╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝─╚═╝╚╝╚══╝╚═══╝╚╝╚╝╚══╝╚═══╝""")
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"-- {x}:{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
print("""
[1] Enable antiban
[2] Disable antiban
""")
select = int(input("-- Select::: "))

if select == 1:
    try:
        sub_client.edit_profile(content=open("content.txt").read())
        print("-- Antiban is enabled!")
    except Exception as e:
        print(e)

elif select == 2:
    try:
        sub_client.edit_profile(content="github.com/deluvsushi")
        print("-- Antiban is disabled...")
    except Exception as e:
        print(e)
