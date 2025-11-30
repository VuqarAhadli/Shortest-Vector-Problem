import math

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def mul(k,v):
    return [k*x for x in v]

def lll_track(B, delta=0.75):
    n = len(B)
    B = [v[:] for v in B]
    Z = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

    k = 1
    while k < n:
        for j in range(k-1,-1,-1):
            mu = dot(B[k], B[j])/dot(B[j], B[j])
            q = round(mu)
            B[k] = sub(B[k], mul(q,B[j]))
            Z[k] = sub(Z[k], mul(q,Z[j]))
        mu_prev = dot(B[k],B[k-1])/dot(B[k-1],B[k-1])
        if dot(B[k],B[k]) >= (delta - mu_prev**2) * dot(B[k-1],B[k-1]):
            k += 1
        else:
            B[k], B[k-1] = B[k-1], B[k]
            Z[k], Z[k-1] = Z[k-1], Z[k]
            k = max(k-1,1)
    return B, Z

def print_vectors(B, Z):
    print("LLL-reduced basis:")
    for i,(v,z) in enumerate(zip(B,Z),1):
        vec = ", ".join(f"{int(round(x)):>3}" for x in v)
        terms = []
        for j, coef in enumerate(z):
            coef = int(round(coef))
            if coef != 0:
                terms.append(f"{coef}*b{j+1}")
        print(f"b{i}: V{{{vec}}}  =  {' + '.join(terms)}")


B3 = [[50,45],[4,3]]
reduced, Z = lll_track(B3)
print_vectors(reduced, Z)

