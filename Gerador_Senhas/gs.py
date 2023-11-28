import random, string

size = 3

chars = string.ascii_letters + string.digits + '!@#$%¨&*()-_=+§ªº/?°;:.>,<'

rand = random.SystemRandom()

print(''.join(rand.choice(chars) for i in range(size)))
