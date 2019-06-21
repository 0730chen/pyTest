# from MyQR import myqr
# myqr.run(words='{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}',picture='1.jpg')
import qrcode
import xlrd
import json
# r'C:\Users\Administrator\Desktop\150个记录.xlsx'
def read():
    work = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\150个记录.xlsx')
    sheet1 = work.sheet_by_name('Sheet1')
    datas = []
    for i in range(1,103):
        x = sheet1.row_values(i)[0]
        data = sheet1.row_values(i)[1]
        # datas.append(data)
        # print(data)
       
        msg = {"name":data,"MAC":data}
        newMsg = json.dumps(msg)
        # type(msg)
        datas.append(newMsg)
    # print(datas[1])
    # print(datas[3])
    return datas
    # def erweima(datas):
    #     for i in range(len(datas)):
    #         print(datas[i])


        # print(Data)
        # print(x)
        # print('新的字符串'+newMsg)
        # print(datas)
    # print(datas)
    # return datas
        # print(datas)
        # return datas
        

    

# qr = qrcode.QRCode(
#         version = 7,
#         error_correction = qrcode.constants.ERROR_CORRECT_L,
#         box_size = 10,
#         border = 4
#     )
def chage(data, i):
    # print(type(data))
    print('开始制作图片')
    qr = qrcode.QRCode(
        version = 7,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    print('我是制作图片中的数据')
    # print(data)
    mess = data
    print(mess)
    qr.add_data(mess)
    qr.make(fit=True)
    img = qr.make_image()
    # # qr.add_data()
    imageName = str(i) + '.jpg'
    img.save(imageName)
    print('图片制作完成')
if __name__ == '__main__':
    read()
    newMess = read()
    number = 0
    # print(newMess)
    # print(newMess[1])
    # chage(newMess[0],0)
    for i in range(len(newMess)):
        # print(newMess[i]+'我是newMess中的数据')
        chage(newMess[i],i)
        
    
        
    
        # print(i) 
    #     qr.add_data(newMess[i])
    #     print(newMess[i])
    #     qr.make(fit=True)
    #     img = qr.make_image()
    #     imageName = str(number) + '.jpg'
    #     number +=1
    #     img.save(imageName)
    # for i in newMess:
        
    #     print(i)
        # number +=1
        # # print(number)
        # chage(i,number)

    # for i in range(0,103):
    #     print(newMess[1])
        # chage(newMess[i],i)
        # chage(newMess[i],i)
    # for i in read():
    #     print(i)
    #  使用字典转换成json字符串{"name": "F9:E:B7:6E:63:B", "MAC": "F9:E:B7:6E:63:B"}
    # {'name':'F9:E:B7:6E:63:B', 'MAC':'F9:E:B7:6E:63:B'}
    # data  = {'name': 'F0:3A:53:84:97:52', 'MAC': 'F0:3A:53:84:97:52'}
    # chage(data)
# data = '{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}'
# qr.add_data(data)
# qr.make( fit=True)
# img = qr.make_image()
# img.save('1.png')

# data = '{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}'
# img_file = r'./1.png'
# img = qrcode.make(data)
# img.save(img_file)
# img.show()