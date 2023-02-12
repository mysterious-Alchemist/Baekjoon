import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a;
		a = sc.nextInt();
		if (a == 0) {
			
		} else if (a != 0) {
			if (10 > a) {
				while (10 >= a) {
					int aa = (2*a)%10;
					a = a*10+(aa);
//					System.out.println(a);
				}

			}
		}

		boolean chk = true;
		int b;
		int c = 0;
		b = a;
		while (chk) {
			int tmp1 = a % 10;
			int tmp2 = a / 10;
			int tmp3 = tmp1 + tmp2;
			if (tmp3 >= 10) {
				tmp3 = tmp3 % 10;
			}
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