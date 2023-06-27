# Yerel Hesap Sıfırlama Programı

Bu Python programı, kullanıcıların unuttukları yerel hesaplarının şifrelerini sıfırlamalarına olanak sağlar. Program, bir komut satırı arayüzü kullanır ve kullanıcılar istedikleri yerel hesabın şifresini sıfırlayabilirler.

**Not: Bu program güvenlik amaçlı kullanılmamalıdır ve yalnızca kayıp veya unutulan hesap şifrelerini geri yüklemek için kullanılmalıdır.**

## Özellikler

- Yerel hesapları listeleme: `--net user` komutunu kullanarak sistemdeki yerel hesapları görüntüler.
- Hesap seçme: Kullanıcı, listelenen hesaplardan birini seçebilir.
- Şifre sıfırlama: Kullanıcı, seçilen hesabın şifresini sıfırlar.

## Kullanım

1. Programı çalıştırmak için aşağıdaki komutu kullanın:


Program çalıştırıldığında, yerel hesapların bir listesi görüntülenecektir.

2. Şifresi sıfırlanacak hesabı seçmek için `--select_account` parametresini kullanın:


Listeden çıkan hesapları görüntüleyerek istediğiniz hesabı seçebilirsiniz.

3. Şifreyi sıfırlamak için seçilen hesabın kullanıcı adını girin:

"username" yerine sıfırlamak istediğiniz hesabın gerçek kullanıcı adını yazın.

4. Şifre sıfırlama işlemi tamamlandığında, program otomatik olarak sonlanacak ve komut satırı kapanacaktır.

**Not: Bu programı kullanmadan önce, güvenlik nedenleriyle mutlaka kullanım koşullarını okuyun ve yalnızca doğru amaçlar için kullanın.**

## Hata Bildirimi

Herhangi bir hata, sorun veya geri bildiriminiz varsa, lütfen bir konu açarak [GitHub Issues](https://github.com/kullaniciadi/proje-adi/issues) üzerinden bildirin. Size yardımcı olmaktan mutluluk duyarız.

## Güvenlik Uyarısı

Bu program, bilinçsiz veya kötü niyetli kullanımlara karşı koruma sağlamaz. Sadece kendi bilgisayarınızda ve uygun izinlerle kullanılmalıdır. Başkalarının hesaplarını izinsiz sıfırlamak veya erişmek yasa dışıdır ve ciddi sonuçlara yol açabilir. Kullanırken lütfen etik kurallara ve yasalara uyun.

## Lisans

Bu program MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyin.
