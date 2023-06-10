"""

เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
    
"""

def main():
    
    numberElements = int(input("Enter number of elements : "))
    
    ary_value = []
    
    for i in range(numberElements):
        ele = int(input("Input number : "))
        ary_value.append(ele)
    
    highest_value = -1

    index_of_highest_value = 0; 

    for value in range(numberElements):
        
        if ary_value[value] > highest_value:
    
            highest_value = ary_value[value]
            index_of_highest_value = value
    
    print("Highest Value Index : {}".format(index_of_highest_value))


if __name__ == '__main__':
    main()