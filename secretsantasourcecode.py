import smtplib, ssl, random, getpass
# This code is for assigning Secret Santa pairings, and emailing out the assignment to each person.
# rules are that no siblings should be matched, and no duplicates

# Class definition here creates People with firstnames, lastnames and emails.
class Person:
    def __init__(self, name, lastname, emailname):
        self.name = name
        self.lastname = lastname
        self.emailname = emailname

# this creates a list and appends each of the people to be added into the list.  To add, simply add more appends
list = []

# this list is of made up names.  Replace names with real ones and email with real one.

list.append(Person("Billy", "Bob", "email@email.com"))
list.append(Person("Jacob", "Bob", "email1@email.com"))
list.append(Person("John", "Doe", "email2@email.com"))
list.append(Person("Brad", "Davis", "email3@email.com"))
list.append(Person("Ryouta", "Takata", "email4@email.com"))
# This looks at the list of names provided, randomizes the list and checks if the last names match.  If they do, it will rerun the shuffle until a list set is found
# where there is no matching pair.  Breakpoint at 100 iterations may need to be adjusted depending on size of list (with size 9 mostly resolved within max 8 iterations
counter = 0
iterations = 0
print("Initial Shuffle")
random.shuffle(list)
iterations = 1
while counter < len(list)-1:
    if list[counter].lastname != list[counter+1].lastname:
#        print(list[counter].lastname)
#        print(list[counter+1].lastname)
        counter+=1
        if counter == len(list)-1:
            if list[0].lastname == list[len(list)-1].lastname:
                counter = 0
                print("Re-Shuffled")
                random.shuffle(list)
                iterations+=1
    else:
        counter = 0
        print("Re-Shuffled")
        random.shuffle(list)
        iterations+=1
        if iterations > 100:
            counter = 100
            print("No pairings possible without matching pairs")

# this mentions how many times the process took (nice to look at to see how many times it had to run) Breakpoint at 100 may need to be changed based on list size
if iterations < 100:
    print("This process took {} times to randomize.".format(iterations))

# This testing code is only for checking to make sure no siblings are matched
# counter2 = 0
# while counter2 < len(list):
#    print(list[counter2].name, list[counter2].lastname)
#    counter2+=1

# this is will create a master file with all the pairings listed.
lengthofarrayrecord = len(list)
counter2 = 0
file = open("records1.txt", "w")
file.write("Here are the pairings: \n \n")

# these variables are for selecting the correct array number (pair 0&1, 1&2 etc)
temp1 = list[0]
temp2 = list[1]
i=0
lengthofarray1 = len(list)


# gmail out setup
port = 587
smtp_server = "smtp.gmail.com"
# put your gmail here
sender_email = "yourgmail@gmail.com"
# password is protected in input using getpass
password = getpass.getpass('Enter Password:')
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    while i < lengthofarray1:
        message = """\
Subject: {} {} Secret Santa Assignment

Hello {} {}.  Your secret santa is: {} {}.""".format(temp1.name, temp1.lastname, temp1.name, temp1.lastname, temp2.name, temp2.lastname)

# this prints where in the array the loop is in.
        print (i)
# this writes the parings each time to the master file
        file.write("{} {} is paired with {} {} \n".format(temp1.name, temp1.lastname, temp2.name, temp2.lastname))
        receiver_email=temp1.emailname
        server.sendmail(sender_email, receiver_email, message)
        if i == lengthofarray1-2:
            temp1 = list[lengthofarray1-1]
            temp2 = list[0]
        if i < lengthofarray1-2:
            temp1 = list[i+1]
            temp2 = list[i+2]
        i+=1
file.close()
print("Emails have been sent and file has been written!")
