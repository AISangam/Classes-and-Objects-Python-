class pad:

    def __init__(self,list1,list2):

        self.list1=list1
        self.list2=list2

    def display(self):

        print("content of list1:",self.list1)
        print("content of list2:", self.list2)

    def padding(self):
        self.pad1 = len(self.list1)-len(self.list2)
        self.pad2 = len(self.list2)-len(self.list1)

        if len(self.list1)== len(self.list2):
            print("Both the list are same and hence no paddding is needed")

        elif len(self.list1)> len(self.list2):
            self.pad_zeros = [0]*self.pad1
            output = self.list2 +self.pad_zeros
            print("Padded list is..",output)

        elif len(self.list1)< len(self.list2):
            self.pad_zeros = [0]*self.pad2
            output = self.list1 +self.pad_zeros
            print("Padded list is..",output)
        else:
            pass


list_1 = input("Enter the numbers for list 1 seperated by whitespace:").split()
list1 = list(map(int,list_1))

list_2= input("Enter the numbers for list 2 seperated by whitespace:").split()
list2 = list(map(int,list_2))

object_pad = pad(list1,list2)
object_pad.padding()