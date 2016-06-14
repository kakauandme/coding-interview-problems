#Write a method that returns all subsets of a set



input = [1,2]


def powerset(elements):
    if len(elements) > 0:
        head = elements[0]
        for tail in powerset(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []


for s in powerset(input):
	print(s)


