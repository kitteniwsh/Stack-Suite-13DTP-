from math import prod
from app import app
from models.extensions import Prime, Composite, db
from itertools import combinations
with app.app_context():
    db.drop_all()
    db.create_all()

def primes(n):
    """https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



x = primes(1000)


PTA = [Prime(value=i) for i in x]

#Obtain all unique pairs of primes (composite numbers such as 8 will not be needed, as rsa relies on the multiplication of two large primes)
all_combinations = [[prod(i), i] for i in list(combinations(x, 2))]
CTA = [Composite(value = i[0]) for i in all_combinations]


#Add the many to many relationship
for i in CTA:
    i.Primes.append(Prime(value = all_combinations[CTA.index(i)][1][0]))
    i.Primes.append(Prime(value = all_combinations[CTA.index(i)][1][1]))

#Commit changes
with app.app_context():
    db.session.add_all(PTA)
    db.session.add_all(CTA)
    db.session.commit()

print("Finished!")
#print(all_combinations[-1])
#Test if combinations works
