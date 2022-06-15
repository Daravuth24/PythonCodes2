def writeuserdetails(username, password):
    f = open("userdetails.txt", "w")
    f.write(username)
    f.write('\n' + password)

writeuserdetails("Daravuth", "Dara@123")