#importing chat file
import chat
while 1==1:
    print"###WELCOME BACK TO SPYCHAT###"
    print"SELECT OPTION"
    print"\t1.LOG IN:\n\t2.SIGN UP:"
    choose = raw_input("")
    if choose == "2" or choose == "2":

        i = False
        while i != True:

            a=raw_input("Mr/Mrs?:")
            b=raw_input("Enter your name:")
            c=raw_input("Enter your age")
            d=raw_input("Enter your rating")
            spy=chat.Name(a,b,c,d)

            spy_name = raw_input("create a username:")# create new user
            spy_password = raw_input("create a passoword:")
            print "running..."
            fob = open("user.txt", 'a')# use filehandling
            fob.write("\n")
            fob.write(spy_name)

            fob.write("\n")
            fob.write(spy_password)
            fob.close()
            break;

    else:
        while 1==1:
            print "\nreading the line file once"
            fob = open("user.txt",'r')
            fob.read()
            raw_input("Enter your user name:"),fob.read()
            raw_input("Enter your password:"),fob.read()
            fob.read()
            fob.close()
            break;



    chat.start_chat()# call start_chat function form chat
