import cv2

#url_cctv = "rtsp://cwem:2025@Admin@192.168.0.12/:554/"
url_cctv = "rtsp://cctvAdmin:2025@Admin@192.168.0.21/:34567/"
cap = cv2.VideoCapture(url_cctv)

if not cap.isOpened():
    print("Gagal akses kamera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal menerima frame (stream berakhir?).")
        break

    width = 1920
    height = 1080
    resized_frame = cv2.resize(frame, (width, height))

    # Menampilkan frame ke jendela
    cv2.imshow('Streaming Kamera OpenCV', resized_frame)

    # Berhenti jika menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Membersihkan sumber daya
cap.release()
cv2.destroyAllWindows()