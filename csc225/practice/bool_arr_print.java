import java.util.Random;

public class bool_arr_print{
	public static void main(String[] args){
		int rows;
		int cols;
		try{
			rows = Integer.parseInt(args[0]);
			cols = Integer.parseInt(args[1]);
		}
		catch(Exception e){
			System.out.println("I made a booboo, yeah");
			return;
		}
		boolean arr[][] = new boolean[rows][cols];
		Random pollock = new Random();

		for (int i = 0; i < rows; i++){
                        for (int j = 0; j < cols; j++){
				arr[i][j] = pollock.nextBoolean();
			}
		}
		for (int i = 0; i < rows; i++){
			for (int j = 0; j < cols; j++){
				if (arr[i][j]) System.out.print("*");
				else System.out.print(" ");
			}
			System.out.println();
		}
	}
}
