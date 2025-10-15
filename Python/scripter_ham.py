
import tensorflow as tf
import numpy as np


skalar = tf.constant(7, name="skalar")
vektor = tf.constant([10, 10], name="vektor")
matriks = tf.constant([[1, 2], [3, 4]], name="matriks")
tensor_float = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float16, name="tensor_float")
tensor_dari_numpy = tf.constant(np.array([[1, 2, 3], [4, 5, 6]]), name="tensor_dari_numpy")

print("--- Informasi Tensor ---")
print("Skalar:", skalar)
print("Vektor:", vektor)
print("Matriks:", matriks)
print("Dimensi Matriks:", matriks.ndim)
print("Bentuk Matriks:", matriks.shape)
print("Tipe Data Matriks:", matriks.dtype)
print("-" * 20)


tensor_op = tf.constant([[1, 2], [3, 4]])

penjumlahan = tensor_op + 10
perkalian = tensor_op * 10
perkalian_matriks = tf.matmul(tensor_op, tensor_op)

print("--- Operasi Tensor ---")
print("Penjumlahan:\n", penjumlahan)
print("Perkalian:\n", perkalian)
print("Perkalian Matriks:\n", perkalian_matriks)
print("-" * 20)

var_ubah = tf.Variable([10, 7], name="variabel_awal")
print("Variabel Awal:", var_ubah.numpy())

var_ubah.assign([1, 2])
print("Variabel Setelah Modifikasi:", var_ubah.numpy())
print("-" * 20)



print("--- Pembangunan dan Pelatihan Model Keras ---")


model = tf.keras.Sequential([
  tf.keras.layers.Dense(128, activation='relu', input_shape=(10,)), 
  tf.keras.layers.Dense(64, activation='relu'),                     
  tf.keras.layers.Dense(10, activation='softmax')                   
], name="model_sederhana")


model.compile(loss=tf.keras.losses.CategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              metrics=['accuracy'])


model.summary()
print("\nMembuat data dummy untuk pelatihan...")
jumlah_sampel = 1000
jumlah_fitur = 10
jumlah_kelas = 10

X_train = tf.random.normal((jumlah_sampel, jumlah_fitur))
y_labels = tf.random.uniform((jumlah_sampel,), maxval=jumlah_kelas, dtype=tf.int32)
y_train = tf.one_hot(y_labels, depth=jumlah_kelas)

print(f"Bentuk X_train: {X_train.shape}")
print(f"Bentuk y_train: {y_train.shape}")

print("\nMemulai pelatihan model...")
histori = model.fit(X_train, y_train, epochs=5, verbose=1)

print("\nMengevaluasi model...")
loss, accuracy = model.evaluate(X_train, y_train, verbose=0)
print(f"Loss setelah pelatihan: {loss:.4f}")
print(f"Akurasi setelah pelatihan: {accuracy:.4f}")

print("\nMelakukan prediksi pada sampel baru...")
sampel_baru = tf.random.normal((1, jumlah_fitur))
prediksi = model.predict(sampel_baru)
kelas_prediksi = tf.argmax(prediksi, axis=1)

print("Prediksi probabilitas:", prediksi)
print("Kelas yang diprediksi:", kelas_prediksi.numpy())