class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.lista = []

    def push(self, x: int) -> None:
        if len(self.lista) < self.maxSize:
            self.lista.append(x)

    def pop(self) -> int:
        if self.lista:
            return self.lista.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.lista))):
            self.lista[i] += val

            
sol = CustomStack(3) #// Stack is Empty []
print(sol.push(1))                        #// stack becomes [1]
print(sol.push(2))                         #// stack becomes [1, 2]
print(sol.pop()   )                        #// return 2 --> Return top of the stack 2, stack becomes [1]
print(sol.push(2)  )                        #// stack becomes [1, 2]
print(sol.push(3)   )                       #// stack becomes [1, 2, 3]
print(sol.push(4)    )                      #// stack still [1, 2, 3], Do not add another elements as size is 4
print(sol.increment(5, 100) )               #// stack becomes [101, 102, 103]
print(sol.increment(2, 100)  )              #// stack becomes [201, 202, 103]
print(sol.pop()               )             #// return 103 --> Return top of the stack 103, stack becomes [201, 202]
print(sol.pop()                )            #// return 202 --> Return top of the stack 202, stack becomes [201]
print(sol.pop()                 )          #// return 201 --> Return top of the stack 201, stack becomes []
print(sol.pop()                  )  