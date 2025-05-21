from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from Crypto.Cipher import AES
import os
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

BLOCK_SIZE = 16

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_file(data, key):
    cipher = AES.new(key.ljust(32, b'0')[:32], AES.MODE_ECB)
    return cipher.encrypt(pad(data))

def decrypt_file(data, key):
    cipher = AES.new(key.ljust(32, b'0')[:32], AES.MODE_ECB)
    return unpad(cipher.decrypt(data))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        key = request.form['key'].encode()
        if uploaded_file.filename != '':
            file_data = uploaded_file.read()
            encrypted_data = encrypt_file(file_data, key)
            return send_file(BytesIO(encrypted_data), as_attachment=True,
                             download_name=secure_filename(uploaded_file.filename + '.aes'))
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        key = request.form['key'].encode()
        if uploaded_file.filename != '':
            file_data = uploaded_file.read()
            decrypted_data = decrypt_file(file_data, key)
            return send_file(BytesIO(decrypted_data), as_attachment=True,
                             download_name='decrypted_' + secure_filename(uploaded_file.filename.replace('.aes', '')))
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
