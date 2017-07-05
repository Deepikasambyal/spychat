# importing chat
import chat

while 1 == 1:
    print"###WELCOME BACK TO SPYCHAT###"
    print"SELECT OPTION"
    print"\t1.LOG IN:\n\t2.SIGN UP:"   # login or signup
    choose = raw_input("")
    if choose == "2" or choose == "2":
        i = False
        while i != True:
            while True:

                a = raw_input("Mr/Mrs?:")    #input  salutation
                if len(a) == 0:
                    print "Invalid value.Re-enter"
                    continue
                b = raw_input("Enter your name:")# input Name
                if len(b) == 0:
                    print "Invalid input.Re-enter"
                    continue
                c = raw_input("Enter your age")# input age
                if c < 18:
                    print "Invalid age"
                    continue
                d = raw_input("Enter your rating") # input rating
                if d < 3:
                    print "Invalid rating.Re-enter(above 3)"
                    continue
                spy = chat.Name(a, b, c, d)
                break

            spy_name = raw_input("create a username:")# create new user
            spy_password = raw_input("create a passoword:")
            print "running..."
            fob = open("user.txt", 'a')# use file handling here to read and write the username and password
            fob.write("\n")
            fob.write(spy_name)

            fob.write("\n")
            fob.write(spy_password)
            fob.close()
            break;
    else:
        while 1 == 1:
            print "\nreading the line file once"
            fob = open("user.txt", 'r')
            fob.read()
            raw_input("Enter your user name:"), fob.read()
            raw_input("Enter your password:"), fob.read()
            fob.read()
            fob.close()
            break;

    chat.msg_check()

