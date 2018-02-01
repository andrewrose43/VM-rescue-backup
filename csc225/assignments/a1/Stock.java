/*
*	Rahnuma Islam Nishat - January 17, 2018
*/
import java.util.Scanner;
import java.io.File;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Stack;

//Simple two-value class to be loaded into the stack for comparison based on "int value"
//int span tracks the span of each price, as defined in the assignment
class Price{
	int span;
	int value;
	public Price(int s, int v){
		this.span = s;
		this.value = v;
	}
}

public class Stock{

	public static int[] CalculateSpan(int[] p){
		int[] s = new int[p.length]; //the destination array

		/*
		//O(n^2) solution (for my future reference)
		for (int i = p.length-1; i>=0; i--){
			s[i] = 1;
			for (int j = i-1; (j>=0 && p[j]<=p[i]); j--) s[i]++;
		}
		//end of O(n^2) solution
		*/

		//O(n) solution
		int spansum; //tracks the span of each Price
		Stack<Price> stk = new Stack<>();
		for (int i = 0; i < p.length; i++){
			spansum = 1; //resetting the Span value to be put into each new Price
			while (!stk.empty() && stk.peek().value<=p[i]){
				spansum += stk.pop().span;
			}
			stk.push(new Price(spansum, p[i])); //push the new Price with the correct span
			s[i] = spansum;
		}	
		//end of O(n) solution

		return s;
	}


	public static int[] readInput(Scanner s){
		Queue<Integer> q = new LinkedList<Integer>();
		int n=0;
		if(!s.hasNextInt()){
			return null;
		}
		int temp = s.nextInt();
		while(temp>=0){
			q.offer(temp);
			temp = s.nextInt();
			n++;
		}
		int[] inp = new int[q.size()];
		for(int i=0;i<n;i++){
			inp[i]= q.poll();
		}
		return inp;
	}
	public static void main(String[] args){
		Scanner s;
        Stock m = new Stock();
        if (args.length > 0){
        	try{
        		s = new Scanner(new File(args[0]));
        	} catch(java.io.FileNotFoundException e){
        		System.out.printf("Unable to open %s\n",args[0]);
        		return;
        	}
        	System.out.printf("Reading input values from %s.\n", args[0]);
        }else{
        	s = new Scanner(System.in);
        	System.out.printf("Enter a list of non-negative integers. Enter a negative value to end the list.\n");
        }
            
        int[] price = m.readInput(s);
        System.out.println("The stock prices are:");
        for(int i=0;i<price.length;i++){
        	System.out.print(price[i]+ (((i+1)==price.length)? ".": ", "));
        }

        if(price!=null){
        	int[] span = m.CalculateSpan(price);
        	if(span!=null){
        		System.out.println("The spans are:");
        		for(int i=0;i<span.length;i++){
        			System.out.print(span[i]+ (((i+1)==span.length)? ".": ", "));
        		}
        	}
        }
    }
}
