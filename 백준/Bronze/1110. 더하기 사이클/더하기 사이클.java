import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a;
		int c = 0;
		a = sc.nextInt();
		int n1 = a % 10;
		int n2 = (a / 10) + (a % 10);
		int n3 = (10 * n1) + (n2 % 10);
		c = c + 1;
		while (a != n3) {
			n1 = n3 % 10;
			n2 = (n3 / 10) + (n3 % 10);
			n3 = (10 * n1) + (n2 % 10);
			c += 1;
		}
		System.out.println(c);
	}
}