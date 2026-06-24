class Order:
    def __init__(self, order_id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""

    def calculate_total_amount(self):
        self.total_amount = self.unit_price * self.quantity + self.shipping_fee - self.voucher

    def classify_order(self):
        if self.total_amount >= 10000000:
            self.order_type = "VIP"
        elif self.total_amount >= 2000000:
            self.order_type = "Lớn"
        elif self.total_amount >= 500000:
            self.order_type = "Trung bình"
        else:
            self.order_type = "Nhỏ"


class OrderManager:
    def __init__(self):
        self.orders = []

    def validate_string(self, value, field):
        if not value.strip():
            print(f"{field} không được rỗng")
            return False
        return True

    def validate_int(self, value, field, min_value=0, max_value=1000000000):
        try:
            num = int(value)
            if num < min_value:
                print(f"{field} không được âm hoặc nhỏ hơn {min_value}")
                return None
            if num > max_value:
                print(f"{field} vượt quá giới hạn {max_value}")
                return None
            return num
        except ValueError:
            print(f"{field} phải là số nguyên")
            return None

    def check_duplicate(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                print("Mã đơn hàng đã tồn tại")
                return True
        return False

    def add_order(self):
        order_id = input("Mã đơn hàng: ").strip()
        if not self.validate_string(order_id, "Mã đơn hàng"):
            return
        if self.check_duplicate(order_id):
            return
        customer_name = input("Tên khách hàng: ").strip()
        if not self.validate_string(customer_name, "Tên khách hàng"):
            return
        product_name = input("Tên sản phẩm: ").strip()
        if not self.validate_string(product_name, "Tên sản phẩm"):
            return
        unit_price = self.validate_int(input("Đơn giá: "), "Đơn giá", 1)
        if unit_price is None:
            return
        quantity = self.validate_int(input("Số lượng: "), "Số lượng", 1)
        if quantity is None:
            return
        shipping_fee = self.validate_int(input("Phí vận chuyển: "), "Phí vận chuyển", 0)
        if shipping_fee is None:
            return
        voucher = self.validate_int(input("Voucher: "), "Voucher", 0)
        if voucher is None:
            return
        order = Order(order_id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher)
        order.calculate_total_amount()
        order.classify_order()
        self.orders.append(order)
        print("Đã thêm đơn hàng thành công")

    def show_all(self):
        if not self.orders:
            print("Danh sách đơn hàng rỗng")
            return
        print(f"{'Mã đơn':<10} | {'Khách hàng':<20} | {'Sản phẩm':<20} | {'Đơn giá':<10} | {'SL':<5} | {'Phí VC':<10} | {'Voucher':<10} | {'Tổng tiền':<15} | {'Loại':<10}")
        print("-" * 120)
        for order in self.orders:
            print(f"{order.order_id:<10} | {order.customer_name:<20} | {order.product_name:<20} | "
                  f"{order.unit_price:<10} | {order.quantity:<5} | {order.shipping_fee:<10} | "
                  f"{order.voucher:<10} | {order.total_amount:<15} | {order.order_type:<10}")

    def update_order(self):
        if not self.orders:
            print("Danh sách đơn hàng rỗng")
            return
        order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
        for order in self.orders:
            if order.order_id == order_id:
                new_quantity = self.validate_int(input("Nhập số lượng mới: "), "Số lượng", 1)
                if new_quantity is None:
                    return
                order.quantity = new_quantity
                order.calculate_total_amount()
                order.classify_order()
                print("Cập nhật thành công")
                return
        print("Không tìm thấy đơn hàng")

    def delete_order(self):
        if not self.orders:
            print("Danh sách đơn hàng rỗng")
            return
        order_id = input("Nhập mã đơn hàng cần xóa: ").strip()
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                print("Xóa thành công")
                return
        print("Không tìm thấy đơn hàng")

    def search_order(self):
        if not self.orders:
            print("Danh sách đơn hàng rỗng")
            return
        order_id = input("Nhập mã đơn hàng cần tìm: ").strip()
        for order in self.orders:
            if order.order_id == order_id:
                print(f"{order.order_id:<10} | {order.customer_name:<20} | {order.product_name:<20} | "
                      f"{order.unit_price:<10} | {order.quantity:<5} | {order.shipping_fee:<10} | "
                      f"{order.voucher:<10} | {order.total_amount:<15} | {order.order_type:<10}")
                return
        print("Không tìm thấy đơn hàng")


def main():
    manager = OrderManager()
    while True:
        print("\n" + "*" * 60)
        print("1. Hiển thị danh sách đơn hàng")
        print("2. Thêm đơn hàng mới")
        print("3. Cập nhật đơn hàng")
        print("4. Xóa đơn hàng")
        print("5. Tìm kiếm đơn hàng")
        print("6. Thoát chương trình")
        print("*" * 60)
        choice = input("Nhập lựa chọn (1-6): ").strip()
        if choice == "1":
            manager.show_all()
        elif choice == "2":
            manager.add_order()
        elif choice == "3":
            manager.update_order()
        elif choice == "4":
            manager.delete_order()
        elif choice == "5":
            manager.search_order()
        elif choice == "6":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
