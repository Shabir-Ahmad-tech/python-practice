# Extract the user name from an email address

email = input("Enter your email address: ")  # input email address

def extract_user_name(email):
    if "@" in email:
        username = email.split("@")[0] # split email at '@' and take the first part
        return username
    else:
        return "Invalid email address"

user_name = extract_user_name(email) # call the function to extract user name
print("User name: " + user_name)      # print the extracted user name