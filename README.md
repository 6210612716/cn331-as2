# cn331-as2

## Members

1. นายพิตตินันท์ เลิศสิริมั่นคง 6210612658
2. นายภูชิชย์ กลีบมาลัย 6210612716

## QuotaApp

#### รายละเอียดการทำงานและการใช้งาน
+ หน้า login สามารถใช้ได้ทั้ง user และ admin เพื่อเข้าสู่หน้า users ต่อไป
+ หน้า users/index หรือหน้า home ซึ่งจะแยกเป็นของ user และ admin โดยจะแสดงข้อมูลพื้นฐานต่าง ๆ เช่น ชื่อ-นามสกุล, รหัสนักศึกษา, email, ปุ่ม logout ส่วนที่แตกต่างกันคือ ของ user จะแสดงรายวิชาที่ได้ลงทะเบียนไปแล้ว และมีปุ่มกดไปหน้า course เพื่อลงทะเบียนรายวิชา ในส่วนของ admin จะแสดงรายชื่อของ user หรือ นักศึกษา ทั้งหมด และจะมีปุ่มให้กดเพื่อไปที่หน้า admin ของ Django
+ หน้า courses จะแสดงรายการของวิชาทั้งหมด โดย user สามารถกดปุ่ม enroll เพื่อลงทะเบียน เมื่อต้องการยกเลิกก็สามารถกดปุ่ม cancel ได้ หากวิชานั้น ๆ โควตาเต็มแล้วจะไม่สามารถกดลงทะเบียนได้ ซึ่งปุ่มจะเปลี่ยนเป็นกดไม่ได้และขึ้นว่า Full เช่นเดียวกับกรณีที่ admin ทำการกดปิดวิชานั้นก็จะไม่สามารถกดลงทะเบียนได้เช่นกัน ซึ่งปุ่มจะเปลี่ยนเป็นกดไม่ได้และขึ้นว่า Closed
+ หน้า admin (ของ Django) admin จะสามารถแก้ไขรายละเอียดของ course ได้ เช่น ตั้งสถานะของ corse ว่าเปิดหรือปิด โดยสามารถเลือกทีเดียวได้หลาย course พร้อมกัน แล้วตั้งสถานะทีเดียวผ่านปุ่ม Action ด้านบนได้
+ Video Link แสดงการทำงานและการใช้งาน https://youtu.be/QU3pgOyGBKI
