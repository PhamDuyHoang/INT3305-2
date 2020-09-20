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

def prob(n,p,r):
   return tohop(n,n+r-1)*pow(p,r)*pow((1-p),n)

def inforMeasure(n, p, N):
  k = tohop(n,n+r-1)*pow(p,r)*pow((1-p),n)
  return -math.log(k, 2)

def sumProb(N, p,r):
    '''
        tuong tu nhu ham sumProb(N,p) cua phan bo binomial
        ham subProb(N,p) cua phan bo binomial cung tiem can den 1 khi n va r tien den vo cung
    '''
    sum = 0
    for i in range(1, N + 1):
      sum = sum + tohop(i,i+r-1)*pow(p,r)*pow((1-p),i)
    return sum
def approxEntropy(N,p,r):
  '''
          Theo kiem chung tu thuc nghiem thi gia tri cua ham approxEntropy cua phan bo negative binomial
          co gia tri lon nha la 0.5

  '''
  sum=0
  for i in range(1, N + 1):
    sum=sum-(math.log(tohop(i,i+r-1)*pow(p,r)*pow((1-p),i),2)*tohop(i,i+r-1)*pow(p,r)*pow((1-p),i))
    return sum

