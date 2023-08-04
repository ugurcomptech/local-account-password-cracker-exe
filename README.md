# Yerel Hesap Sıfırlama Programı

Bu Python programı, unutulan yerel hesap şifrelerini sıfırlamak veya silmek için kullanılan bir araçtır. Program, komut satırı arayüzü üzerinden çalışır ve kullanıcıların istedikleri yerel hesabın şifresini sıfırlamalarını veya silmelerini sağlar.

## Özellikler

- Yerel hesapları listeleme: Program, `net user` komutunu kullanarak sistemdeki yerel hesapları görüntüler.
- Hesap şifresini sıfırlama: Kullanıcı, seçtiği yerel hesabın şifresini boş olarak sıfırlayabilir.
- Hesabı silme: Kullanıcının seçitği yerel hesabı silebilir.

## Nasıl Kullanılır

1. Programı çalıştırmak için sağ tık yapıp yönetici olarak çalıştır deyin:
Program çalıştırıldığında, sistemdeki yerel hesapların bir listesi görüntülenecektir.

2. Şifresi sıfırlanacak hesabın kullanıcı adını girin:
`username` yerine sıfırlamak istediğiniz hesabın gerçek kullanıcı adını yazın.

3. Şifre sıfırlama işlemi tamamlandığında, program tarafından bir mesaj görüntülenecektir.

## Uyarılar

- **Güvenlik**: Bu program, sadece kendi hesaplarınızda veya izin verilen sistemlerde kullanılmalıdır. Başka kişilere ait hesapların şifrelerini izinsiz olarak sıfırlamak yasa dışıdır.
- **Önemli**: Exeye sağ tıklayıp yönetici olarak çalıştırmayı unutmayın yoksa herhangi bir şifre sıfırlama veya silme işlemi gerçekleşmez.
- **Hatalar**: Python dosyasının düzgün çalışabilmesi için, Python'un sistemde yüklü olması gerekmektedir. Ayrıca, bazı işletim sistemleri veya güvenlik ayarları, programın yerel hesap şifrelerini sıfırlamasını engelleyebilir.

## Hata Bildirimi

Eğer herhangi bir hata veya sorunla karşılaşırsanız, lütfen bize bildirin. Hata bildirimlerinizi GitHub üzerinden yapabilirsiniz. Daha fazla bilgi için [Hata Bildirim Rehberi](CONTRIBUTING.md) dosyasına göz atın.

## Katkıda Bulunma

Bu program açık kaynaklıdır ve katkıda bulunmak isteyen herkesin katılımına açıktır. Yeni özellikler eklemek, hataları düzeltmek veya programın performansını artırmak için GitHub üzerinden katkıda bulunabilirsiniz. Daha fazla bilgi için [Katkıda Bulunma Kılavuzu](CONTRIBUTING.md) dosyasını inceleyin.

## Lisans

[![License: GPL](https://img.shields.io/badge/License-GPL-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



Bu projeyi [GNU Genel Kamu Lisansı (GPL)](https://www.gnu.org/licenses/gpl-3.0) altında lisansladık. Lisansın tam açıklamasını [GNU web sitesinde](https://www.gnu.org/licenses/gpl-3.0) bulabilirsiniz.

