#arbitary arguments
#using(* arys)

def add(*num):
    sum=0
    for n in num:
        sum=sum+n
        
    print("sum:",sum)
add(34,4,1,2)
add(1,2,3,4)

#using(**kwargs)
def my_fun(**kid):
    print("his last name is " +kid["lname"])
my_fun(fname="arul",
       lname="mozhi")

