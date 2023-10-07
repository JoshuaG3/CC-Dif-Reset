from cryptography.fernet import Fernet

# read encrypted pwd and convert into byte
with open('encryptedPWD.txt') as f:
    encpwd = ''.join(f.readlines())
    encpwdbyt = bytes(encpwd, 'utf-8')
f.close()

# read key and convert into byte
with open('refKey.txt') as f:
    refKey = ''.join(f.readlines())
    refKeybyt = bytes(refKey, 'utf-8')
f.close()

# use the key and encrypt pwd
keytouse = Fernet(refKeybyt)
myPass = (keytouse.decrypt(encpwdbyt))

passStr = str(myPass, encoding="utf-8")

print(passStr)