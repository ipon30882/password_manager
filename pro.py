import hashlib

def hash_password(username, password):
    # สร้างวัตถุ hash แบบ SHA-256
    hash_object = hashlib.sha256()

    # อัปเดตวัตถุ hash ด้วยชื่อผู้ใช้งานและรหัสผ่านที่ให้มา
    hash_object.update(password.encode('utf-8'))

    # รับค่าแฮชเป็นรหัสผ่านที่ถูกแฮชแล้ว
    hashed_password = hash_object.hexdigest()

    return hashed_password

print("----menu-----")
print("1) Signup")
print("2) Login")
print("3) Quit")
print("-------------")
choice = input("Choose: ")

if choice == '1':
    # รับชื่อผู้ใช้งานและรหัสผ่านจากผู้ใช้
    username = input("กรุณาใส่ชื่อผู้ใช้งาน: ")
    password = input("กรุณาใส่รหัสผ่าน: ")

    # แฮชรหัสผ่านพร้อมกับชื่อผู้ใช้งาน
    hashed_password = hash_password(username, password)

    # บันทึกลงในไฟล์ข้อความ
    with open("hashed_password.txt", "w") as file:
        file.write(username + ":" + hashed_password)

    print("ชื่อผู้ใช้งานและรหัสผ่านถูกแฮชและบันทึกลงในไฟล์ hashed_password.txt เรียบร้อยแล้ว")

elif choice == '2':
    # ล็อกอินเข้าระบบ
    username = input("กรุณาใส่ชื่อผู้ใช้งาน: ")
    password = input("กรุณาใส่รหัสผ่าน: ")

    # อ่านข้อมูลจากไฟล์ hashed_password.txt
    with open("hashed_password.txt", "r") as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(":")
            if username == stored_username and hash_password(username, password) == stored_hashed_password:
                print("ล็อกอินสำเร็จ")
                break
        else:
            print("ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง")

elif choice == '3':
    print("ออกจากโปรแกรม")

else:
    print("เลือกไม่ถูกต้อง")
