import json, os


def insert(id):
    all_data = []
    data = {
        "id" : id,
        "name": input("enter name: "),
        "age": int(input("enter age:")),
        "gender":input("enter gneder:")
    }

    if os.path.exists("crud.json"):
        with open("crud.json", "r") as f:
            all_data = json.load(f)
            for stored_data in all_data:
                if stored_data['id'] == data['id']:
                    print("User already exists with this id!")
                    return

    all_data.append(data)
    with open("crud.json", "w") as f:
        json.dump(all_data, f, indent=4)
    print("data inserted successfully!")
 

def read():
    if os.path.exists("crud.json"):        
        with open("crud.json", "r") as f:
            all_data = f.read()
            if all_data != "":
                print(all_data)
                return
    print("database is empty")

def update(id):
    if os.path.exists("crud.json"):
            
        with open("crud.json", "r") as f:
            all_data = json.load(f)

            for data_to_update in all_data:
                if data_to_update['id'] == id:
                    
                    data_to_update["name"] = input("update name: ")
                    data_to_update["age"] = int(input("update age: "))
                    data_to_update["gender"] = input("update gender: ")
                    
                    with open("crud.json", 'w') as f:
                        json.dump(all_data, f, indent=4)
                    return
            else:
                print("invalid input id")
    else:
        print("database is empty. Insert something first.")

def delete(id):
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


choice = int(input("choose: "))

if choice == 1:
    with open("crud.json", "r") as f:
        all_data = json.load(f)
        maxId = 0
        for data in all_data:
            if data["id"] > maxId:
                maxId = data['id']
        insert(maxId+1)
if choice==2:
    id = int(input("Enter your id: "))
    update(id)

