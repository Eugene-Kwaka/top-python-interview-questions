# ## *args
# def add(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print("Sum:", add(1,2))
# print("Sum:", add(1,2,3,4,5))
# print("Sum:", add(10,20,30,40,50,60,70,80,90))

## **kwargs
def startup(**employees):
    total_emps = 0
    # 
    for num in employees.values():
        total_emps += num
    return total_emps

print("Total employees at the startup are:", startup(frontend=2, backend=3, ux=2, cto=1))
