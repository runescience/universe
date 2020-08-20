package com.jdspub.games;

public class PairOfDice {

//            public PairOfDice() {
//                    // Constructor.  Rolls the dice, so that they initially
//                    // show some random values.
//                roll();  // Call the roll() method to roll the dice.
//            }
//            
//	public int roll() {
//		// Roll the dice by setting each of the dice to be
//		// a random number between 1 and 6.
//		List myArray;
//
//		int die1 = (int) (Math.random() * 6) + 1;
//		// System.out.println(die1 +","+die2 );
//		return die1;
//	}
	
	public Integer roll() {
		// Roll the dice by setting each of the dice to be
		// a random number between 1 and 6.

		int dice = (int) (Math.random() * 6) + 1;
		return dice;
	}

	public int rollArray(int quan) {
		// Roll the dice by setting each of the dice to be
		// a random number between 1 and 6.
			
			//System.out.printf("in showGold()");
			int sum = 0;
			for (int ii = 0;ii<quan;ii++) {
				sum += (int) (Math.random() * 6) + 1;
			}
			return sum;
		
	}

} // end class PairOfDice
