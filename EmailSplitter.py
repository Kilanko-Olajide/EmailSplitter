email = input("Enter your email you want to split: ")

username, domain = email.split("@")
print(f"Your username: {username}\nYour domain: {domain}")


'''
I figured out an alternative way to do this is
email = input("Enter your email you want to split: ")

index = email.index("@")
username = email[:index]
domain = email[index+1:]

print(username)
print(domain)

'''
