# import cProfile
# import pstats
import time 

print(time.time())
# def add(x,y):
#     result = 0
#     result += x
#     result += y
#     return result

# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result

# def do_stuff():
#     result = []
#     for i in range(100000):
#         result.append(i)
#     return result

# def waste_time():
#     time.sleep(3)
#     print("Done wasting time")


# if __name__ == "__main__":
#     # with cProfile.Profile() as profile:  
#     profile = cProfile.Profile()
#     print(add(100,400))
    
#     profile.enable()
#     print(fact(1500))
#     profile.disable()
    
#     profile.enable()
#     print(do_stuff())
#     profile.disable()
    
    
#     # print(waste_time())
    
#     result_stats = pstats.Stats(profile).strip_dirs().sort_stats('tottime')
#     result_stats.print_stats()
    
#     # profile.print_stats(2)

#     # result = pstats.Stats(profile).sort_stats(pstats.SortKey.TIME)
#     # result.print_stats(10)
    
    
    
 