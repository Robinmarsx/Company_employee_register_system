import mmse_dev
# login = mmse_dev.login()

UserType = mmse_dev.login()
log = {1: "customer service", 2: "senior customer service", 3: "financial manager", 4: "administration manager",
       5: "service manager", 6: "production manager", 7: "sub-team", 8: "HR"}
# print(log.keys())
if UserType in log.keys():
    print('\n')
    print('\n')
    print('\n')
    print("Success,"+" "+"this account is a "+log[UserType])
else:
    print('\n')
    print('\n')
    print('\n')
    print("Error")

