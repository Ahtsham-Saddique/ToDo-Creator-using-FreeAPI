# create_to_do.py
# fetch_to_do_list.py
import requests
import json

def create_todo():
    url = "https://api.freeapi.app/api/v1/todos/"

    title=input("Enter the title  : ")
    discription=input("Enter discription : ")
    is_complete=input("ENter O/1")
    is_complete=bool(int(is_complete))
    

    # Sample todo data (you can customize or take input)
    todo_data = {
        "title": title,
        "description":discription,
        "isComplete": is_complete
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(todo_data))
    data = response.json()

    if data.get("success"):
        created = data["data"]
        print("✅ Todo created successfully!")
        print(f"Title       : {created['title']}")
        print(f"Description : {created.get('description', '')}")
        print(f"Completed   : {created['isComplete']}")
        print(f"Created At  : {created['createdAt']}")
    else:
        print(" Failed to create ToDo")
        print("Message:", data.get("message"))

def main():
    try:
        create_todo()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
