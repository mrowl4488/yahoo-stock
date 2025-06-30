# yahoo-stock
อย่าลืม download pyhon มาก่อน

ติดตั้ง packages ตามด้านล่างนี้
pip install pandas
pip install yfinance
pip install matplotlib

ชื่อหุ้นสามารถปรับเปลี่ยนได้จาก
symbol = 'AAPL' #Exsample AAPL, NVDA and AMZN ให้ใส่ตัวย่อหุ้นใน '....'

ถ้าจะ downloand ไฟล์ CVS ให้ ลบ# ในบรรทัดสุดท้าย
#data.to_csv(r'C:/Users/Admin/Desktop/Coder/AAPL_data.csv') #Save csv to desktop #you can delete "#" to save csv file. ลบ "#" ข้างหน้าบรรทัดจะเชฟไฟล์ CSV ได้
