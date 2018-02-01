public class mystery{

	public static int m(int a, int b){
		if (b==0) return 0;
                if (b%2 == 0) return m(a+a, b/2);
                return m(a+a, b/2)+a;
	}

	public static void main(String[] args){
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		System.out.println(m(a,b));
	}
}
