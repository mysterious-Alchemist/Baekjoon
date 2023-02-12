import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a;
		a = sc.nextInt();
		boolean chk = true;
		if (a==0) {
			chk = true;
//			System.out.println(1);
		}
		else if (10 > a) {
			while (10 >= a) {
				a = a * 10 + ((2 * a) % 10);
//					System.out.println(a);
			}
		}

		
		int b;
		int c = 0;
		b = a;
		while (chk) {
			int tmp1 = a % 10;
			int tmp2 = a / 10;
			int tmp3 = (tmp1 + tmp2)%10;
			a = tmp1 * 10 + tmp3;
			c = c + 1;
//			System.out.println(a + " " + b + " " + c);
			if (a == b) {
				chk = false;
				System.out.println(c);
			}
		}
	}
}