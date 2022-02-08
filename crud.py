import json, os

def insert(id):
    all_data = []
    data = {
        "id" : id,
        "username": input("enter username: "),
        "surname": input("enter surname:"),
        "password": input("enter password:")
    }

    with open("crud.json", "r") as f:
        all_data = json.load(f)

    all_data.append(data)
    with open("crud.json", "w") as f:
        json.dump(all_data, f, indent=4)
    print("data inserted successfully!")
 

def read_by_Id():
    if os.path.exists("crud.json"):        
        with open("crud.json", "r") as f:
            all_data = f.read()
            if all_data != "":
                print(all_data)
                return
    print("database is empty")


def update_by_Id(id):
    if os.path.exists("crud.json"):
            
        with open("crud.json", "r") as f:
            all_data = json.load(f)

            for data_to_update in all_data:
                if data_to_update['id'] == id:
                    
                    data_to_update["username"] = input("update username: ")
                    data_to_update["surname"] = input("update surname: ")
                    data_to_update["password"] = input("update password: ")
                    
                    with open("crud.json", 'w') as f:
                        json.dump(all_data, f, indent=4)
                    return
            else:
                print("invalid input id")
    else:
        print("database is empty. Insert something first.")


def delete_by_Id(id):
    if os.path.exists("crud.json"):
            
        with open("crud.json", "r") as f:
            all_data = json.load(f)

            for data_to_delete in all_data:
                if data_to_delete['id'] == id:
                    all_data.remove(data_to_delete)
                    with open('crud.json', "w") as f:
                        json.dump(all_data, f, indent=4)
                        print("data deleted successfully!")
                    return
            else:
                print("invalid input id")
    else:
        print("database is empty. Insert something first.")

print("1) Insert \n2) Update_By_ID\n3) Read\n4) Delete_By_ID")
choice = int(input("choose any one:-  "))

if choice == 1:
    if os.path.exists("crud.json"):
        with open("crud.json", "r") as f:
            all_data = json.load(f)
            maxId = len(all_data)+1
    else:
        with open("crud.json","w") as f:
            f.write('[]')
            maxId = 1
    insert(maxId)

elif choice==2:
    id = int(input("Enter your id: "))
    update_by_Id(id)

elif choice == 3:
    read_by_Id()

elif choice == 4:
    Id = int(input("Enter your id:-"))
    delete_by_Id(Id)
else:
    print("invalid input:-") 
