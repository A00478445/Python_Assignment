# Q1
def stack(our_list, operation, new_element):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop()
        else:
            print("Stack is empty, cannot perform remove operation.")
    else:
        print("Invalid operation. Please use 'add' or 'remove'.")

def queue(our_list, operation, new_element):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
        else:
            print("Queue is empty, cannot perform remove operation.")
    else:
        print("Invalid operation. Please use 'add' or 'remove'.")

# Result:
new_list = [1,2,3,4]
print("Adding a new element to the stack")
stack(new_list,'add',5)
print(new_list)
print("Removing an element from the stack")
stack(new_list,'remove',None)
print(new_list)
print("Adding a new element to the queue")
queue(new_list,'add',5)
print(new_list)
print("Removing an element from the queue")
queue(new_list,'remove',None)
print(new_list)




