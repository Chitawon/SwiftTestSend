
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numberThaiText = ["ศูนย์", "หนึ่ง", "สอง", "สาม",  "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

unitNumber =  [1, 10, 100, 1000, 10000, 100000, 1000000]
unitNumberThaiText = ["หน่วย", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]


def main():

    inputNumber = -1
    
    while inputNumber < 0 or inputNumber >= 10000000:
        
        inputNumber = int(input("Input number to convert : "))
        
        if inputNumber < 0:
            print("Input negative number. Please input postive number.")
        elif inputNumber >= 10000000:
            print("Input over limit number. Please input number lower then 10 million.")
    
    thaiTextAns = ""
    
    if inputNumber == 0:
        thaiTextAns += GetThaiText(inputNumber, 0)
    else:
        thaiTextAns = FindAmountNmber(inputNumber)
    
    print(thaiTextAns)

def FindAmountNmber(number):
    
    unitLength = len(unitNumberThaiText) - 1
    
    ansText = ""
    
    while number:
        
        unitAmonut = number // unitNumber[unitLength]
        
        if unitAmonut == 0:
            unitLength -= 1
            continue
        
        ansText += GetThaiText(unitAmonut, unitLength)
        
        number -= (unitAmonut * unitNumber[unitLength])
        
        unitLength -= 1
    
    return ansText
    
def GetThaiText(amount, unit):

    numberThaiIndex = number.index(amount)
    
    unitText = ""
    
    if unit != 0:
        unitText = unitNumberThaiText[unit]
    
    
    thaiText = numberThaiText[numberThaiIndex] + unitText
    
    return thaiText
    
if __name__ == '__main__':
    main()