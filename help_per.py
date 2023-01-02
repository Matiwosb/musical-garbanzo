class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def __repr__(self):
        return repr(self.data)

stack = Stack() # call the class

print('is empty? ', stack.is_empty()) # if is empty

stack.push('first in') # append things
stack.push('second')
stack.push('third')
stack.push('last in')

print(stack) # straight call class if __repr__

print('is empty? ', stack.is_empty())

last_item = stack.pop()
print(f'pop the stack, the item is, "{last_item}"') # remove first item