def product_recurcive(x,y):
    if y > x:
        (x,y) = (y,x)
    if y == 0 :
        return 0
    y -= 1 
    return x + product_recurcive(x,y)

a = 500
b = 2000
print(a*b)
print(product_recurcive(a,b))