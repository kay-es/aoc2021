lines = [eval(line) for line in open('18/sample.txt', 'r')]


def reduce(elements, first_ref=None, second_ref=None, hierarchy=1):
    for i, elem in enumerate(elements):
        first_ref = elements[i-1] if i > 0 else None
        second_ref = elements[i+1] if i < len(elements)-1 else None
        if isinstance(elem, list):
            if hierarchy > 3:
                explode(elem, first_ref, second_ref)
            else:
                reduce(elem, first_ref, second_ref, hierarchy+1)
    return []



def magnitude():
    pass

def split(elements, i, parents):
    pass

def explode(elements, first_ref, second_ref):
    if not first_ref is None:
        while isinstance(first_ref, list):
            first_ref = first_ref[1]
        first_ref += elements[0]
    if not second_ref is None:
        while isinstance(second_ref, list):
            second_ref = second_ref[0]
        second_ref += elements[1]

def addition(left, right):
    return [left] + right

test = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
reduce(test)
exit()
result = lines[0]
for line in lines[1:]:
    result = addition(result, line)
    result = reduce(result)

print(result)