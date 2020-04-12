"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.

For example, given input strings = ['ab', 'ab', 'abc'] and query = ['ab', 'abc', 'bc'] , we find 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, we add an element to our return array,[2, 1, 0] .
"""


strings = ['ab', 'ab', 'abc']
querys = ['ab', 'abc', 'bc']


result = []
for i in querys:
    count = strings.count(i)
    result.append(count)

print(result)