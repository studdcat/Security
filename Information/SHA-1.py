##### SHA-1

# from hashlib import sha1
# import random

# t=1
# while(t==1):
#     thash = str(random.randint(10000000,99999999))+"salt_for_you"
#     temp = thash
#     for i in range(0,500):
#         thash = sha1(thash.encode('utf-8')).hexdigest()
    
#     if (thash == "48df44120d72fb68bc2748474c2e4cbc96edbc51"):
#         print(temp)
#         t=0



from hashlib import sha1

file = open("C:/Users/kisec/Desktop/raindow.txt", "w")

for i in range(10000000, 20000000):
    hash = str(i) + "salt_for_you"

    for j in range(500):
        string = sha1(hash.encode('utf-8')).hexdigest()

    file.write(str(i) + ' : ' + string[:8] + "\n")
    
file.close()