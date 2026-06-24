class Order:
    def __init__(self, order_id, customer_name,product_name,unit_price, quantity,shipping_fee,voucher):
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity 
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""
    def calculate_total_amount(self):
        # tổng tiền = đơn giá * số lượng + phí vận chuyển - voucher
        total_amount = self.unit_price * self.quantity + self.shipping_fee 
    def classify_order(self):
        # nếu đơn hàng có tổng tiền từ >= 10000000 thì vip 
        # nếu đơn hàng có tổng tiền từ >= 2000000 thì lớn 
        # nếu đơn hàng có tổng tiền từ >= 500000 thì trung bình 
        if self.total_amount >= 10000000 :
            self.classify_order = "VIP"
        elif self.total_amount >= 2000000 :
            self.classify_order = "Lớn"
        elif self.total_amount >= 500000 :
            self.classify_order = "Trung bình"
        else: 
            self.classify_order = "Nhỏ"
            return 
class OrderManager: 
    def __init__(self):
        self.orders = []
        return
    def add_order(self, order_id, customer_name,product_name,unit_price, quantity,shipping_fee,voucher):
        user = str(input("Cho người dùng nhập tên:")).strip()
        self.order_id = order.id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity 
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        return 
    print("Đã thêm thành công !")
    def show_all(self):
        if order == "":
            print("Thông báo: Danh sách đơn hàng đang rỗng!") 
        if order.id == order.id: 
            print("Mã số đã tồn tại , quý khách vui lòng nhập lại!")
        for order in self.orders :
            if order.id == order.id: 
                print(f"{"Mã đơn hàng:":<10} | {"Tên khách hàng:":<30} | {"Tên sản phẩm:":< 20} | {"Đơn giá:":< 10} | {"Số lượng":<15} | {"Phí vận chuyển:":< 15} | {"Voucher:":< 10} | {"Tổng tiền:":< 20} | {"Phân loại đơn hàng:" :< 25}")
                continue
            if order.id != order.id:
                print(f"{"Mã đơn hàng:":<10} | {"Tên khách hàng:":<30} | {"Tên sản phẩm:":< 20} | {"Đơn giá:":<10} | {"Số lượng:":<15} | {"Phí vận chuyển:":<15} | {"Voucher:":< 10} | {"Tổng tiền:":< 20} | {"Phân loại đơn hàng:":< 25}")
                return 
            print("Thông báo hiển thị thành công !")
    def update_order(self):
        pass
        print("Cập nhật đơn hàng thành công!")
    def delete_order(self):
        pass
        print("Xóa thành công")
    def search_order(self):
        pass
        print("Tìm kiếm thành công!")
    def validate_order(self):
        pass
def main():
    order = OrderManager()
    print("*" *60)
    print("            MENU              ")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới ")
    print("3.Cập nhật đơn hàng")
    print("4.Xóa đơn hàng")
    print("5. Tìm kiếm đơn hàng")
    print("6.Thoát chương trình") 
    print("*" * 60)
    choice = int(input("Người dùng vui lòng nhập lựa chọn từ 1- 6:"))
    match(choice):
        case"1":
            self.add_order = add_order()
        case "2":
            self.show_all = show_all()
        case "3":
            self.update_order = update_order()
        case "4":
            self.delete_order = delete_order()
        case"5":
            self.search_order = search_order()
        case "6":
            print("Thoát chương trình")
        case _:
            return
if __name__ == "main":
    main()