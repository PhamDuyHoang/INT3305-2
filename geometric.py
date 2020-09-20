import math
def prob(n,p):
    return p*pow((1-p),n-1)

def inforMeasure(n,p):
    k=p*pow((1-p),n-1)
    return -math.log(k,2)


def sumProb(N,p):
    '''
      Ham subProb(N,p) co the su dung de kiem chung
      tong xac suat cua phan bo geometric bang 1
      vd: voi sumProb(3,0.6)=0.936
      neu ta tang n tu 3 len 7 ta se duoc sumProb(7,0.6)=0.9983616
      va neu cu tang dan n len den vo cung thi gia tri cua ham
      sumProb(N,p) se tiem can den gia tri 1 va
      co the the noi neu n= vo cung va voi bat ky gia tri nao cua
      p tu 0 den 1 thi sumProb(N,p) se bang 1
      '''
    sum=0
    for i in range(1,N+1):
        sum=sum+p*pow((1-p),i-1)
    return sum

def approxEntropy(N,p):
    '''
        Ham approxEtropy(N,p) tinh xap xi entropy cua nguon thong tin geometric
        vd: ta co approxEntropy(5,0.5)=1.78125 xap xi voi entropy cua nguon thong tin geometric
        thuc nghiem ta co voi approxEntropy(3,0.5)=1.375 neu tang dan N tu 3 len den vo cung
        thi gia tri cua ham approxEntropy se tiem can den 2 voi moi p tu 0 den 1
    '''
    sum=0
    for i in range(1,N+1):
        sum=sum-(math.log(p*pow((1-p),i-1),2)*p*pow((1-p),i-1))
    return sum




    


