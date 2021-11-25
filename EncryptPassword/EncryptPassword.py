import base64
from guizero import App, Text, TextBox, PushButton

def EncryptPassword():
    global String_Encrypted_Password
    # takes password
    password_as_string = textbox.value
    print(password_as_string)
    # encrypts the password
    Encrypted_Password = base64.b64encode(password_as_string.encode("utf-8"))
    print(Encrypted_Password)
    # converts encrypted password from binary to a string
    String_Encrypted_Password = Encrypted_Password.decode("utf-8")
    print(String_Encrypted_Password)



def DecryptPassword():
    global String_Encrypted_Password
    Encrypted_Password = String_Encrypted_Password.encode("utf-8")
    print(Encrypted_Password)
    Decrypted_Password = base64.b64decode(Encrypted_Password.decode("utf-8"))
    print(Decrypted_Password)
    String_Decrypted_Password = Decrypted_Password.decode("utf-8")
    print(String_Decrypted_Password)


app = App()
text = Text(app, text = "\nPassword: ")
textbox = TextBox(app, width= 20)
button = PushButton(app, text= "Encrypt", command=EncryptPassword)
button1 = PushButton(app, text="Decrypt", command=DecryptPassword)

print(base64.b64encode("password".encode("utf-8")))
print(base64.b64decode(b'cGFzc3dvcmQ='.decode("utf-8")))
#
#
#convert binary to string'
password1 = base64.b64encode("pass".encode("utf-8"))
print(password1)
blobvarstr = base64.b64decode(password1.decode('utf-8'))
print(blobvarstr)
app.display()

