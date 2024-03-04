# Déclaration de la classe MyEmptyStackException
class MyEmptyStackException(Exception):
    pass

# Déclaration de la classe MyOutOfSizeException
class MyOutOfSizeException(Exception):
    pass

# Déclaration de la classe MyStack
class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1
        self.element_1 = None
        self.element_2 = None
        self.element_3 = None  # Ajoutez autant d'éléments que nécessaire

    def add_to_stack(self, item):
        """Ajoute un élément au sommet de la pile."""
        if self.is_full():
            raise MyOutOfSizeException("The stack is full")
        self.top += 1
        if self.top == 0:
            self.element_1 = item
        elif self.top == 1:
            self.element_2 = item
        elif self.top == 2:  # Modifiez ce nombre en fonction du nombre d'éléments maximum
            self.element_3 = item
        else:
            raise MyOutOfSizeException("The stack is full")

    def pop_from_stack(self):
        """Retire et retourne l'élément du sommet de la pile."""
        if self.is_empty():
            raise MyEmptyStackException("The stack is empty")
        if self.top == 0:
            item = self.element_1
            self.element_1 = None
        elif self.top == 1:
            item = self.element_2
            self.element_2 = None
        elif self.top == 2:  # Modifiez ce nombre en fonction du nombre d'éléments maximum
            item = self.element_3
            self.element_3 = None
        self.top -= 1
        return item

    def is_empty(self):
        """Renvoie True si la pile est vide, sinon False."""
        return self.top == -1

    def is_full(self):
        """Renvoie True si la pile est pleine, sinon False."""
        return self.top == self.max_size - 1

# Exemple d'utilisation
if __name__ == "__main__":
    size = int(input("Entrez la taille de la pile : "))
    myStack = MyStack(size)
    myStack.add_to_stack('hello')
    myStack.add_to_stack('world')
    print(myStack.is_full()) # False
    myStack.add_to_stack('!')
    print(myStack.is_full()) # True
    try:
        myStack.add_to_stack('extra') # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)
    print(myStack.pop_from_stack()) # !
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # world
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # True
    try:
        print(myStack.pop_from_stack()) # MyEmptyStackException
    except MyEmptyStackException as e:
        print(e)
