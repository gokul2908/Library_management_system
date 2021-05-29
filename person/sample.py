from datetime import datetime

then = datetime.now()
x = input("wait")
now = datetime.now()


difference = now - then
print(difference.days)

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)


x = ["gokul"]
if x:
    print(3)