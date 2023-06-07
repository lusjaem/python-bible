students = {
    "Alice" : {"id":"ID0001", "age":26, "grade":"D"},
    "Bob" : {"id":"ID0002", "age":27, "grade":"A"},
    "Claire" : {"id":"ID0003", "age":21, "grade":"C"},
    "Dan" : {"id":"ID0004", "age":24, "grade":"B"},
    "Emma" : {"id":"ID0004", "age":25, "grade":"E"}
}
'''
print(students["Dan"]["age"])
print(students["Emma"]["id"],students["Emma"]["grade"])
print(students)
'''
print(list(students)[3::1])