import java.util.Scanner;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashSet<Integer> set = new HashSet<>();
		for (int i=0; i<10; i++) {
			int num;
			num = sc.nextInt();
			int rst = num % 42;
			set.add(rst);
//			System.out.println(num+" "+rst);
		} 
		System.out.println(set.size());
	}
}