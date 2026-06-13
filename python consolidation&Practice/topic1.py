
def find_user(user_id):
    users = [
        {"id":1,"name":"Hanna"},
        {"id":2,"name":"John"}
    ]

    for user in users:
        if user["id"] == user_id:
            return user

    return {"error": "User not found"}

print(find_user(1))


from fastapi import FastAPI

app=FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return find_user(user_id)
print(find_user(1))



class UserNotFoundError(Exception):
    pass
def get_user(user_id):
    if user_id != 1:
        raise UserNotFoundError("User not found")
    return{"id":1}
try:
    print(get_user(5))
except UserNotFoundError as e:
    print(e) 



from fastapi import FastAPI, HTTPException

app=FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):

    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    
    return {
        "id":1,
            "name":"Hanna"
    }




