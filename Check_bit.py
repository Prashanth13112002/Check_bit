class solution:
    def check_bit(self,a,b):
        if a&(1<<b):
            return 1
        else:
            return 0
a1=solution()
a=int(input())
b=int(input())
print(a1.check_bit(a,b))