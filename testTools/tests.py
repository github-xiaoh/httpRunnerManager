from django.test import TestCase



a = '{0},{1},{2}'.format('sdsd','222','333')

print(a)



a = {}
b = []
c = [2,3,4]

for i in c:
    print(i)
    a['q'] = i
    print(a)
    b.append(a)
    a={}
    print(b)


x = {'q':3,'a':4,'h':5,'o':'p'}
y = {'q':3}
query = '&'.join([f'{k}={x[k]}' for k in sorted(x)])
print(query)


ui = 1630425600000
print(int(ui/1000))



# Create your tests here.
