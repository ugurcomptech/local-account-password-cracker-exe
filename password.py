import subprocess

def reset_local_accounts():
    print("Yerel hesapları sıfırlama aracına hoş geldiniz!")
    list_local_accounts()
    selected_account = input("Sıfırlanacak hesabın kullanıcı adını girin: ")
    reset_account_password(selected_account)
    input("Devam etmek için bir tuşa basın...")  # Komut satırının kapatılmasını engellemek için bekleme yapılıyor.

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

if __name__ == "__main__":
    reset_local_accounts()
