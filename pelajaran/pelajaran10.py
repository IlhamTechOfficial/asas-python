import os
import hashlib
import binascii
import getpass


def main():

    def encrypt(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')


    def decrypt(stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


    # paswd = 'abc123!'
    # encrypted_paswd = encrypt(paswd)
    # print(encrypted_paswd)
    encrypted_paswd = 'c2e1f6f1ee12c6567ceb70c0906bc89b488489d3464c255ce8442a8bc78165648c433c82ad07693bb7d17b00f1c413fb11375979f2c0a50088a3b8d739db529448d4f0372f20e09131659f0d2724cbc16dd6c3143122d505265d1c9b1540947d'
    jumlah_cubaan = 3

    # while True:
    #     paswd_input = input('Masuk pasword anda: ')
    #     if decrypt(encrypted_paswd, paswd_input):
    #         print('Login dengan sukses')
    #         break
    #     else:
    #         print('Login gagal. Sila cuba semula')

    jumlah_cubaan_yang_tinggal = jumlah_cubaan
    for cubaan in range(jumlah_cubaan):
        print("Jumlah cubaan yang tinggal ialah: ", jumlah_cubaan_yang_tinggal)
        paswd_input = getpass.getpass('Masuk password anda: ')
        if decrypt(encrypted_paswd, paswd_input):
            print('Login dengan sukses')
            print("Anda sudah berada di laman utama")
            break
        else:
            print('Login gagal. Sila cuba semula')
            jumlah_cubaan_yang_tinggal = jumlah_cubaan_yang_tinggal - 1

        if jumlah_cubaan_yang_tinggal == 0:
            print("Anda telah habis jumlah cubaan untuk login.")
    
    
    print('main END')


if __name__ == '__main__':
    main()