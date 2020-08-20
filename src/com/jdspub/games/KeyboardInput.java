package com.jdspub.games;
import java.util.Scanner;

public class KeyboardInput {
	public static void main(String[] args) {

		String stuff = new KeyboardInput().getString("Enter String:");

		System.out.println(stuff);
		
		PairOfDice pd = new PairOfDice();
		pd.roll();
		
	}

	private static String getString(String title) {
		// TODO Auto-generated method stub
		System.out.print(title);
		Scanner scanner = new Scanner(System.in);
		String inputString = scanner.nextLine();
		return inputString;
	}

}