import secrets;a=('0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','@');m=[]
for i in range(32):m.append(secrets.choice(a))
print(''.join(m))#this!!!!!