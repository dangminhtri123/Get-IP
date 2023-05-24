import socket

def get_wifi_ip():
    # Tạo một socket mới
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Kết nối tới một địa chỉ IP bất kỳ (ở đây chúng ta sử dụng Google DNS)
        sock.connect(("8.8.8.8", 80))

        # Lấy địa chỉ IP của máy tính
        wifi_ip = sock.getsockname()[0]
        return wifi_ip
    except Exception as e:
        print("Không thể lấy địa chỉ IP WiFi (vui lòng thử lại hoặc kiểm tra đường truyền kết nối):", e)
    finally:
        sock.close()

# Gọi hàm để lấy địa chỉ IP WiFi
ip = get_wifi_ip()

# Hiển thị banner
print("TOOL GET IP WIFI PLATIC")
print("")

# Hiển thị địa chỉ IP WiFi
print("Địa chỉ Wifi của bạn:", ip)

