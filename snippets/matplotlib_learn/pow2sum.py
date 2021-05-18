def power(n,p):
    val = n**p
    return val

def power_sum_list(lst,p):
    sm=0
    for k in lst:
        sm+=power(k,p)
    return sm

def get_user_input():
    start = input("please input start number:")
    end = input("please input end number:")
    p = input("please input power number")

    start = int(start)
    end=int(end)
    p = float(p)
    return start,end,p

if __name__ == "__main__":
    start,end,p= get_user_input()
    if(start>end):
        raise ValueError("start can not be little than end")
    lst = range(start,end+1,1)
    sm = power_sum_list(lst,p)
    print("the power sum between %d %d of %f is %f"%(start,end,p,sm))