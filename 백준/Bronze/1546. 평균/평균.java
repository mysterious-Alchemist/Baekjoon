import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String sub_num;
		sub_num = sc.nextLine();
		String input = sc.nextLine(); //sc.nextInt()로 받으면 에러 발생
		String[] inputValues = input.split(" "); 
		List<Double> subject = Arrays.stream(inputValues) //소수점을 요구하기 때문에 더블로 
		  .map(Double::parseDouble)                       //스트림<<<유용함
		  .collect(Collectors.toList());
		Double max = Collections.max(subject);            // 최댓값 뽑아냄
		for (int i=0; subject.size()>i; i++) {            // 리스트의 경우 .size() .get() 사용
		    double a = subject.get(i);
		    subject.set(i, a*100/max);
		}
		double sum = subject.stream().mapToDouble(Double::doubleValue).sum(); //아직 잘 모르겠음
//		System.out.println(sub_num);
		System.out.println(sum/Integer.parseInt(sub_num));
	}
}