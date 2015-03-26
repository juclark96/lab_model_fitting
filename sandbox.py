def foo() :
    print "Hello World"
    
foo()

var = "comme"

def woo( x ):
    print var,
    print x,
    
woo("ci,")
woo("ca.")

def factorial( n ):
    prod = 1
    for i in range(1,n+1):
        prod= prod*i
    return prod
factorial( 2 )
print factorial (2)