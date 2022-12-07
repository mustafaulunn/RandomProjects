package MainPackage;
import UserPackage.*;
import java.util.*;
public class MainClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		UserIslem KullanciIslem = new UserIslem();
		Scanner dvm = new Scanner(System.in);	
		Scanner anaMenu = new Scanner(System.in);
		int menu;
		int dd = 0;
		do {
			System.out.println("Programamiza hosgeldiniz..");
			System.out.println("[1] - Giris");
			System.out.println("[2] - Yeni Kayit");
			System.out.println("[3] - Sifre Degisterme");
			menu = anaMenu.nextInt();
			
			if(menu == 1) {
				KullanciIslem.UserGiris();
			}else if (menu == 2){
				KullanciIslem.yeniKayit();	
			}else if(menu == 3) {
				KullanciIslem.changeSifre();
			}
			
			System.out.println("Devam etmek istiyormusun? [0-Evet/ 9-Hayir]");
			dd = dvm.nextInt();
		} while (dd == 0);
	}
}
