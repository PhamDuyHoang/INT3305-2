import math
def gt(n):
    k = 1;
    if (n == 0 or n == 1):
        return k
    else:
        for i in range(2, n + 1):
            k = k * i
        return k
def tohop(k,n):
    return int(gt(n)/(gt(n-k)*gt(k)))

def prob(n,p,N):
    return tohop(n,N)*pow(p,n)*pow((1-p),N-n)

def inforMeasure(n,p,N):
    k=tohop(n,N)*pow(p,n)*pow((1-p),N-n)
    return -math.log(k, 2)

def sumProb(N,p):
    '''
        tuong tu nhu ham sumProb(N,p) cua phan bo geometric
        ham subProb(N,p) cua phan bo binomial cung tiem can den 1 khi n tien den vo cung
    '''
    sum = 0
    for i in range(1, N + 1):
        sum=sum+tohop(i,N)*pow(p,i)*pow((1-p),N-i)
    return sum

def approxEntropy(N,p):
    '''
        Theo kiem chung tu thuc nghiem thi gia tri cua ham approxEntropy cua phan bo binomial
        se chay tiem can den 3 khi n tien den vo cung gia tri nay cung xap xi voi gia tri entropy cua phan bo binomial
    '''
    sum=0
    for i in range(1,N+1):
        sum=sum-(math.log(tohop(i,N)*pow(p,i)*pow((1-p),N-i),2)*tohop(i,N)*pow(p,i)*pow((1-p),N-i))
    return sum



