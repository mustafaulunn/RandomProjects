package UserPackage;
import java.util.*;
public class UserIslem {
	public String uAdi = "Ali";
	public String uSifre = "123";
	public String gKodu = "123456789";
	
	public void UserGiris() {
		Scanner uGiris = new Scanner(System.in);

		System.out.println("Kullanci giris islem..");
		System.out.print("Kullanci Adi: ");
		String kAdi = uGiris.nextLine();
		System.out.print("Kullanci Sifre: ");
		String kSifre = uGiris.nextLine();		
		
		if((!uAdi.equals(kAdi))){
			System.out.println("Kullanci adi hatali..");
		}		
		if((!uSifre.equals(kSifre))){
			System.out.println("Kullanci Sifre hatali..");
		}		 
	}	
	public void changeSifre() {
		Scanner uPC = new Scanner(System.in);
		System.out.println("Kullanci sifre degisterme islem..");
		System.out.print("Guvenilk  Kodu: ");
		String gCode = uPC.nextLine();
		if(("123456789".equals(gCode))){
			System.out.println("Yeni Sifre giriniz..");
			String ySif = uPC.nextLine();
			uSifre = ySif;
			System.out.println("Sifre degistrme islem basarli..");
		}else
		{
			System.out.println("guvenlik kodu yanlis..");
		}
	}
	public void yeniKayit() {
		System.out.println("Yeni Kullanci islem..");
	}
}
