public class Euclid{

	public static int traceEuclid(int p, int q){
		System.out.println("p = " + p + ", q = " + q);
		
		if (q==0) return p;
		int r = p%q;
		return traceEuclid(q, r);
		
	}

	public static void main(String[] args){
		int p, q;
		try{
			p = Integer.parseInt(args[0]);
			q = Integer.parseInt(args[1]);
		}
		catch(Exception e){
			System.out.println("Oops");
			return;
		}
		System.out.println("The GCD is " + traceEuclid(p,q));
	}
}
