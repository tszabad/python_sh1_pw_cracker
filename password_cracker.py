import hashlib

def crack_sha1_hash(hash, use_salts=False):
  
  with open('top-10000-passwords.txt', 'r') as f:
    f = f.read().splitlines()
    if use_salts==True:
      pass
    
	  
    else:
      passwords = []
      for line in f:
        new_hash = hashlib.sha1(line.encode()).hexdigest()
        if new_hash== hash:
          passwords.append(line)
          print(line)
          return line
      if len(passwords)<1:
        return "PASSWORD NOT IN DATABASE"
      
      
        
            


