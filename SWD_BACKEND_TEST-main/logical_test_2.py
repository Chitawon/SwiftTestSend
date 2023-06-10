
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

roman_number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman_text = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

def main():
    
    input_number = -1
    
    while input_number <= 0 or input_number > 1000:
        
        input_number = int(input("Input number to convert : "))
        
        if input_number <= 0:
            print("Input negative number. Please input postive number.")
        elif input_number > 1000:
            print("Input over limit number. Please input number lower then 10 million.")
    
    
    list_lenght = len(roman_text) - 1

    roman_ans = ""

    while input_number:
        
        romanTextAmount = input_number // roman_number[list_lenght]
    
        roman_ans += GetRomanText(romanTextAmount, roman_text[list_lenght])
    
        input_number -= romanTextAmount * roman_number[list_lenght]
        list_lenght -= 1

    print(roman_ans)

def GetRomanText(amount, text):
    
    romanText = ""
    
    for x in range(amount):
        romanText += text
    
    return romanText

if __name__ == '__main__':
    main()
    
