List1= [1,3,2]
List2= [12,18,23]
List3= [41,11,26]

List4= [List1, List2, List3]

def find_max(List4):
    max_value= List4[0][0]
    for list in List4:
        for x in list:
            if x>max_value:
                max_value= x
    return max_value
max_value= find_max(List4)
print("The maximum value is: ", max_value)


global my_stack

my_stack= []
my_queue= []

def my_push(x):
    global stack
    my_stack= [*my_stack, 55]
    return my_stack

def my_pop():
    global my_stack
    value = my_stack[-1]
    my_stack= my_stack[:-1]
    return value

def my_enqueue(x):
    global my_enqueue
    my_queue= [x, *my_queue]
    return my_queue

def my_dequeue():
    global my_queue
    value= my_queue[0]
    my_queue= my_queue[1:]
    return value

print(my_push(55))
print(my_push(78))
print(my_push(22))
print(my_pop())
print(my_enqueue(55))
print(my_enqueue(78))
print(my_enqueue(22))
print(my_dequeue())
print(my_dequeue())

    


