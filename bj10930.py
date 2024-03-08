#!/usr/bin/env python

import hashlib
n=input().rstrip()
hash_object=hashlib.sha256()
hash_object.update(n.encode())
hash_value=hash_object.hexdigest()
print(hash_value)

