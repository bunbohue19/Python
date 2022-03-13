from collections import defaultdict

new_defaultdict = defaultdict(set)

new_defaultdict['Five'].add(5)
new_defaultdict['Ten'].add(10)
new_defaultdict['Five'].add('5')
new_defaultdict['Ten'].add("10")
new_defaultdict['Fifteen']

print(dict(new_defaultdict.items()))

new_defaultdict2 = defaultdict(list)

new_defaultdict2['Five'].append(5)
new_defaultdict2['Ten'].append(10)
new_defaultdict2['Five'].append('5')
new_defaultdict2['Ten'].append("10")
new_defaultdict2['Fifteen']

print(dict(new_defaultdict.items()))
