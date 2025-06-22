# n=int(input())
# arr=list(map(int,input().split()))
# result=0
# for i in range (32):
#     bit_count=0
#     for num in arr:
#         if (num>>i)&1:
#             bit_count+=1
#     if bit_count %3==2:
#         result |=(1<<i)
# if result>=2**31:
#     result-=2**32
# print(result)

# n=int(input())
# arr=list(map(int,input().split()))
# result=[]
# for i in range(n):
#     found=-1
#     for j in range (i+1,n):
#         if arr[j]< arr[i]:
#             found=arr[j]
#             break
#     result.append(found)
# print(*result)

s=input("enter the string: ")
print(s[::-1].capitalize())
