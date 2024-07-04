def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def insecure_function():
    secret = "my_secret_password"
    print(secret)

if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    insecure_function()

