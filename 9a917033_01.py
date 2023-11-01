x=int(input("請輸入星星數量："))
a= int ((x+1)/2)
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1)+" "*(a-i))
for k in range(a-1,0,-1):
    print(" "*(a-k)+"*"*(2*k-1)+" "*(a-k))