import subprocess

def reset_local_accounts():
    print("Yerel hesap işlemlerine hoş geldiniz!")
    while True:
        print("1 - Hesap sıfırlama")
        print("2 - Hesap silme")
        print("0 - Çıkış")
        choice = input("Yapmak istediğiniz işlemi seçin (0-2): ")
        
        if choice == "1":
            list_local_accounts()
            selected_account = input("Sıfırlanacak hesabın kullanıcı adını girin: ")
            reset_account_password(selected_account)
        elif choice == "2":
            list_local_accounts()
            selected_account = input("Silmek istediğiniz hesabın kullanıcı adını girin: ")
            delete_account(selected_account)
        elif choice == "0":
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
        
        input("Devam etmek için bir tuşa basın...")

def list_local_accounts():
    print("Yerel hesaplar:")
    subprocess.run("net user", shell=True, check=True)
    print()

def reset_account_password(username):
    reset_command = f"net user {username} \"\""
    try:
        subprocess.run(reset_command, shell=True, check=True)
        print(f"{username} hesabının parolası sıfırlandı.")
    except subprocess.CalledProcessError:
        print(f"{username} hesabının parolası sıfırlanırken bir hata oluştu.")

def delete_account(username):
    try:
        subprocess.run(f"net user {username} /delete", shell=True, check=True)
        print(f"{username} hesabı başarıyla silindi.")
    except subprocess.CalledProcessError:
        print(f"{username} hesabının silinirken bir hata oluştu.")

if __name__ == "__main__":
    reset_local_accounts()
