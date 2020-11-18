#RANDOM

import random
for i in range(10):
     x = random.random()
     print(x)

import random
print(random.randint(5, 10))

import random
t=(1,2,3)
print(random.choice(t))

# Random.seed se utiliza para tener siempre el mismo random (utilizado para testear)
import random
random.seed(1,1)
print(random.randint(5, 10))
