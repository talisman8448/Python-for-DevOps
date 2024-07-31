import sys

instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("Okay, We will launch the t2.micro type instance for you!")
else:
    print("Sorry, we will not be able to launch the instance with this type, as you are using free tier account!")


