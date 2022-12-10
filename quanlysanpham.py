"""
ứng dụng quản lí chi tiêu chco phép thêm, sửa, xóa
list gồm các sản phẩm

product = {
    "name": "sua rua mat"
    "value" : 200000
    "input_day": 18/11/2022
    "out_put": <Nếu có>
    "loai_san_pham": mỹ phẩm
}

"""
def them(list_of_products, product):
    list_of_products.append(product)

def xem(list_of_products):
    for product in list_of_products:
        print(product)
        
def xoa(list_of_products, name):
    index = -1
    for i in range(len(list_of_products)):
        if ten == product[i]["name"]:
            index = i 
            break
        if index == -1:
            print("Không tìm thấy sản phẩm", name)
        else: 
            list_of_products.remove(product[index])
    
list_of_products = []

while True:
    yeu_cau = int(input("Ấn 1 để xem danh sách sản phẩm\
                    Ấn 2 để thêm sản phẩm\
                    Ấn 3 để xóa sản phẩm"))
    if (yeu_cau == 1): 
        print("Hiện thị danh sách sản phẩm")
        xem(list_of_products)
    elif (yeu_cau ==2):
        print("Thêm sản phẩm mới")
        name = input("Nhập vào tên sản phẩm: ")
        value = int(input("Nhập vào giá trị của sản phẩm: "))
        input_day = input("Nhập vào ngày nhập sản phẩm: ")
        output_day = input("Nhập vào ngày xuất: ")
        loai_san_pham = input("Loại sản phẩm: ")
        product= {
            "name": ten,
            "value": value,
            "input_day": input_day,
            "output_day": output_day,
            "loai_san_pham": loai_san_pham,
        }
        them(list_of_products, product)
    elif (yeu_cau == 3):
        print("Xóa 1 sản phẩm")
        ten = input("Nhập vào tên sản phẩm cần xóa:")
        xoa(list_of_products, name)
    else: 
        print("Bạn nhập vào không đúng yêu cầu")
    y_o_n = input("Bạn muốn tiếp tục [Y/N]?: ")
    if y_o_n.upper() == "N":
        break