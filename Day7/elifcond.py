import sys

instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("Okay, we will launch the instance for you but, this will charge you $2/day!")
elif instance_type == "t2.medium":
    print("Okay, we will launch the instance for you but, this will charge you $4/day!")
elif instance_type == "t2.large":
    print("Okay we will launch the instance for you but, this will charge you $6/day!")
else:
    print("Oops, Please provie valid instance type!")
 