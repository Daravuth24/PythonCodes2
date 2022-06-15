def createmyfile():
    # myfile = open("./files/firstfile.txt", "x") x, r, w means create mode
    # print(myfile)
    myfile = open("testfile.txt", "a")
    print(myfile)

    myfile.write("\n This is new statement")

createmyfile()