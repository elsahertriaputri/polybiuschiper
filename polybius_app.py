import streamlit as st

def polybius_encrypt(message):
    """Fungsi enkripsi Polybius Cipher 5x5."""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # "J" digabungkan dengan "I"
    message = message.upper().replace(" ", "").replace("J", "I")
    cipher_text = ""

    # Enkripsi setiap karakter
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            row = index // 5 + 1
            col = index % 5 + 1
            cipher_text += str(row) + str(col)
    return cipher_text

def polybius_decrypt(cipher_text):
    """Fungsi dekripsi Polybius Cipher 5x5."""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    message = ""

    # Dekripsi setiap pasangan angka
    for i in range(0, len(cipher_text), 2):
        row = int(cipher_text[i]) - 1
        col = int(cipher_text[i+1]) - 1
        index = row * 5 + col
        message += alphabet[index]
    return message

# Streamlit App
st.title("Polybius Cipher Encryptor & Decryptor")

st.sidebar.header("Input")
option = st.sidebar.radio("Pilih operasi:", ["Enkripsi", "Dekripsi"])
message = st.sidebar.text_input("Masukkan pesan (tanpa spasi):", "")

if st.sidebar.button("Proses"):
    if message:
        if option == "Enkripsi":
            cipher_text = polybius_encrypt(message)
            st.success(f"Teks terenkripsi: {cipher_text}")
        elif option == "Dekripsi":
            if len(message) % 2 != 0:
                st.error("Pesan yang didekripsi harus memiliki panjang genap (setiap angka harus berpasangan).")
            else:
                decrypted_text = polybius_decrypt(message)
                st.success(f"Teks terdekripsi: {decrypted_text}")
    else:
        st.error("Harap masukkan pesan yang ingin dienkripsi atau didekripsi.")
