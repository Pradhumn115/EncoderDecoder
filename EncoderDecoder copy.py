
import string
import random



def encodingmessage(message):

        if (len(message)>=3):
            temp = message[0]
            message = message[1:len(message)]+temp
            text =""
            for i in range(6):
                text += ("".join(random.choices(string.ascii_lowercase)))

            message = text[0:3] + message + text[3:6]
        elif(len(message)<3 and len(message)>0):
            message = message[::-1]

        print(message)
        return message

def decodingmessage(message):
    if (len(message)<3 and len(message)>0):
        message = message[::-1]
    elif(len(message)>=3):
        message = message[3:len(message)-3]
        message = message[-1]+message[:-1]

    print(message)
    return message


while True:
    message = input("Enter Message: ")
    if (message == "exit()"):
        break

    elif (message == ""):
        print("No Message")
        continue
    else:
        rtext = encodingmessage(message)
        decodingmessage(rtext)
