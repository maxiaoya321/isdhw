Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(1,10):
        for k in range(0,i-1):
            print(end="        ")
        for j in range(i,10): 
            print(str.format("{0:1}*{1:1}={2:>2}",i,j,i*j),end="  ")
        print()
