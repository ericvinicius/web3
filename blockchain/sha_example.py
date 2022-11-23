import hashlib

def main():
    txt = "Ola Mundo".encode('utf-8')
    secret_thing = hashlib.sha256(txt)
    
    print("SHA 256")
    print(secret_thing.hexdigest())
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()