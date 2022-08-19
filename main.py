class Node():
    def __init__(self, data):
        self.data = data
        self.pointer = ""
        
    def get_data(self):
        return self.data
    
    def get_pointer(self):
        return self.pointer
    
    def set_pointer(self, pointer):
        self.pointer = pointer

class Linked_List():
    def __init__(self):
        self.start = Node("Head")
        
    def display_data(self):
        current_node = self.start
        index = 0

        print(f"{'index':^10}|{'data':^10}")
        while current_node != "":
            print(f"{index:<10}|{current_node.get_data():<10}")
            current_node = current_node.get_pointer()
            index += 1

    def insert_node(self, data):
        new_node = Node(data)
        previous_node = self.start
        current_node = previous_node.get_pointer()
        
        if current_node == "":
            previous_node.set_pointer(new_node)
        else:
            while True:
                if current_node == "" or data < current_node.get_data():
                    previous_node.set_pointer(new_node)
                    new_node.set_pointer(current_node)
                    return
                previous_node = current_node
                current_node = current_node.get_pointer()

    def delete_node(self, data):
        previous_node = self.start
        current_node = previous_node.get_pointer()

        while True:
            if current_node == "":
                return "ValueError: list.remove(x): x not in list"
            if current_node.get_data() == data:
                previous_node.set_pointer(current_node.get_pointer())
                return
            previous_node = current_node
            current_node = current_node.get_pointer()

    def reverse_list(self):
        previous_node = self.start
        current_node = previous_node.get_pointer()
        next_node = current_node.get_pointer()

        while next_node != "":
            if previous_node == self.start:
                current_node.set_pointer("")
            else:
                current_node.set_pointer(previous_node)
            previous_node = current_node
            current_node = next_node
            next_node = next_node.get_pointer()
        current_node.set_pointer(previous_node)
        self.start.set_pointer(current_node)

    def get_middle_node(self):
        current_node = self.start
        middle_node = current_node
        even_odd = 0
        
        while current_node != "":
            if even_odd == 0:
                even_odd = 1
                middle_node = middle_node.get_pointer()
            else:
                even_odd = 0
            current_node = current_node.get_pointer()
        return middle_node.get_data()
            

l = Linked_List()
for data in [5, 4, 6 ,17, 3, 0]:
    l.insert_node(data)
l.display_data()
