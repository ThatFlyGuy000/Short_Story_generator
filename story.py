import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','Once Upon a time']
who = ['A Rabbit', 'An Elephant', 'A mouse', 'A turtle','A cat']
name = ['Alan', 'Baloo','Manny', 'Swiper', 'Skywalker']
residence = ['Barcelona','Forest', 'Germany', 'Venice', 'suburbs']
went = ['Movie theatre', 'University','seminar', 'school', 'laundry Shop','Amusement Park']
happened = ['made a lot of friends','had its food stolen', 'found a secret key', 'solved a mystery', 'wrote a book','found a four leaf clover',]
print(random.choice(when) + ', ' + random.choice(who) + ' living in ' +  random.choice(residence) +  '  who went by the name  ' +random.choice(name)+', went to the ' + random.choice(went) + ' and ' + random.choice(happened))