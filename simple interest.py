def simple_interest (p, t, r):
    print("principle:",p)
    print("time:",t)
    print("rate of interest:",r)
    
    si=(p*t*r)/100
    print(si)
    return si

p=float(input("Enter the principle "))
t=float(input("Enter the time "))
r=float(input("Enter the rate of interest "))
simple_interest (p,t,r)