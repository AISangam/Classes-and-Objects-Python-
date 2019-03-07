#padding class is created
class pad:
# init function is used to initialize the value of the variable used in the program. Please refer to the below link for more details
#https://qr.ae/TWXnYc
    
    def __init__(self,list1,list2):
  #these are values of the objects and self is the current object which is having such value.
        self.list1=list1
        self.list2=list2

   #display the value of the list1 and list2
    
    def display(self):
        print("content of list1:",self.list1)
        print("content of list2:", self.list2)
   #function padding is made 
    def padding(self):
        self.pad1 = len(self.list1)-len(self.list2)
        self.pad2 = len(self.list2)-len(self.list1)
   #comparison test for the padding is done here for each case.
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

#user will enter the numbers to make the list
list_1 = input("Enter the numbers for list 1 seperated by whitespace:").split()
#map the strings in the list to integers
list1 = list(map(int,list_1))
#user will enter the numbers to make the list
list_2= input("Enter the numbers for list 2 seperated by whitespace:").split()
#map the strings in the list to integers
list2 = list(map(int,list_2))
#object is created for the class pad
object_pad = pad(list1,list2)
#function padding is called using the above created object
object_pad.padding()
