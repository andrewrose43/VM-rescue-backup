import java.util.Scanner;
public class int_to_binarystr{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		String s = "";
		for (int i = N; i > 0; i /= 2)
			s = (i%2)+s;
		System.out.println(s);
	}
} 
