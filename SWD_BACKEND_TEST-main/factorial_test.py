"""

เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว   

"""

def main():

    factorial_number_input = int(input("Factorial Input number : "))
    
    factorial_result = factorial_find(factorial_number_input)
    
    print(factorial_result)
    
    print("Have Zero : {}".format(find_zero(factorial_result)))

def factorial_find(num):
    sum = 1
    
    if num == 0:
        return 1
    
    for value in range(1, num + 1):
        sum *= value
    
    return sum

def find_zero(num):
    list_number = [int(x) for x in str(num)]
    
    factorial_zero = 0
    
    for x in range(len(list_number) - 1, -1, -1):
        
        if list_number[x] != 0:
            break
        
        factorial_zero += 1
    
    return factorial_zero
          
if __name__ == '__main__':
    main()