def createStack():
    stack = [] 
    return stack

def isEmpty(stack):
    return len(stack) == 0 

def top(stack):
    return stack[-1]

def pop(stack):
    p = stack.pop()
    return p 

def push(stack,e):
    stack.append(e)

def print_stack(stack):
    for p in stack:
        print(p)
def sortStack(stack):
    tmpStack = createStack()
    push(tmpStack,pop(stack))
    while (isEmpty(stack) == False):
        p = pop(stack)
        while (isEmpty(tmpStack) ==False and top(tmpStack) >p):
            push(stack,pop(tmpStack))
        push(tmpStack,p)
    return tmpStack
    


if __name__ =='__main__':
    a = createStack()
    push(a,3)
    push(a,5)
    push(a,1)
    push(a,4)
    a = sortStack(a)
    print_stack(a)


