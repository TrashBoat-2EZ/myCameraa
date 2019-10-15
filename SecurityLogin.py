user = "Finn"
password = "P@ssword#1"


def test_input():
    if user == "Finn":
        if password == "P@ssword#1":
            print("Correct")
        else:
            print("Wrong Password")
    elif password == "P@ssword#1":
        if user != "Finn":
            print("Wrong Username or Password")
    else:
        print("INCORRECT")


test_input()
