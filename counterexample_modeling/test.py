import hashlib
text_1 = 'G(F(switch=off&Fa=1))'
text_2 = 'G(F(switch=off&Fa=2))'
print(int(hashlib.sha1(text_1.encode()).hexdigest(), 16) % (10**8))
print(int(hashlib.sha1(text_2.encode()).hexdigest(), 16) % (10**8))