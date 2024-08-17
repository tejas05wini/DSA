n=int(input("enter the total number of students "))

def accept_marks(A):
      print("Enter -1 for Absent Students")
      for i in range(0,n):
          x=int(input("Enter the percentage of %d student "%(i+1)))
          A.append(x)
   

def display_marks(A):

      print("FDS PERCENTAGE REPRESENTATION")
      for i in range(0,n):
        if(A[i]!=-1):
           print("The percentage of",(i+1), "student is ", A[i])
        else:
           print("Student ",(i+1)," is absent ")


def average_marks(A):
    sum=0
    for i in range(n):
        if(A[i]!=-1):
            sum+=A[i]
        avg=sum/n 
    print("Average score of the class is ",avg)

def maximum_marks(A):
    max=0
    for i in range (0,n):
        if(A[i]!=-1 and max<A[i]):
            max=A[i]
    print("Maximum score of class is ",max)

def minimum_marks(A):
    min=100
    for i in range(0,n):
        if(A[i]!=-1 and A[i]<min):
            min=A[i]
    print("Minimum score of class is ",min)

def absent_count(A):
    count=0
    for i in range(0,n):
        if(A[i]==-1):
            count=count+1
    print("No. of absent students are ",count )


def max_freq(A):
    count=0
    for i in range(0,n):
        freq=0
        for j in range(0,n):
            if(A[i]==A[j] and A[i]!=-1):
                freq=freq+1
            if(count<freq):
                count=freq
                ele=A[i]
    print("NO OF STUDENTS OF SCORING MAX MARKS ",A[i],"ARE" ,freq)




def main():
    A=[]
    accept_marks(A)
    display_marks(A)
    average_marks(A)
    minimum_marks(A)
    maximum_marks(A)
    absent_count(A)
    max_freq(A)
main()