import hashlib

def crack_sha1_hash(hash, use_salts=False):
  
  with open('top-10000-passwords.txt', 'r') as f:
    passwords = []
    f = f.read().splitlines()
    if use_salts==True:
      
      with open("known-salts.txt", 'r') as ks:
        ks = ks.read().splitlines()
        for line in f:
          for salt in ks:
            new_hash1 = hashlib.sha1((line+salt).encode()).hexdigest()
            new_hash2 = hashlib.sha1((salt+line).encode()).hexdigest()
            new_hash3 = hashlib.sha1((salt+line+salt).encode()).hexdigest()
            if new_hash1 == hash or new_hash2 == hash or              new_hash3 == hash:
              print(line)
              return line
	  
    else:
      for line in f:
        new_hash = hashlib.sha1(line.encode()).hexdigest()
        if new_hash== hash:
          passwords.append(line)
          print(line)
          return line
          
    if len(passwords)<1:
      return "PASSWORD NOT IN DATABASE"
      
      
      
        
            


