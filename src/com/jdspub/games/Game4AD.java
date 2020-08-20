package com.jdspub.games;
import java.util.ArrayList;
import java.util.Scanner;

public class Game4AD {
	//MyNewInfoPacket packet = new MyNewInfoPacket(null);

	PairOfDice pd = new PairOfDice();
	boolean isFinal = false;
	String lastAction = "";

	public static void main(String[] args) {

		// System.out.println(new Game4AD().getMinion());
		// System.out.println(new Game4AD().doCorridor());
		// System.out.println(new Game4AD().doRoom());
		// System.out.println(new Game4AD().getMapPiece());

		String token = "hello";

		switch (token) {
		case "one":
			break;
		case "hello":
			System.out.println("\n hello \n");
			break;
		case "two":
			break;
		}

		new Game4AD().doIt();
	}

	private void doIt() {
		// Java example

		String result = "";

		Scanner keyboard = new Scanner(System.in);

		while (true) {
			//System.out.printf("*doIt(): lastAction=%s result=%s \n", lastAction, result);
			System.out.printf("*>>  %s \n", result);

			if (result.equals("empty"))
				System.out.println("\nYour next action? (getMAP, getROOm, getCoRRidor,rooMLIST,SEArch,quit)");
			else
				System.out.println("\nYour next action? (getMap, getRoom, getCorridor,roomlist,quit)");

			String action = "";
			action = keyboard.next();

			// System.out.printf("in doIt():%s\n", action);

			if (containsIgnoreCase("quit", action)) {
				System.out.println("Thanks for playing! Bye!\n===!\n\n");
				System.exit(0);

			} else if (containsIgnoreCase("getMap", action)) {
				result = getMapPiece();


			} else if (containsIgnoreCase("1", action)) {
				result = r1();

			} else if (containsIgnoreCase("2", action)) {
				result = r2();

			} else if (containsIgnoreCase("3", action)) {
				result = r3();

			} else if (containsIgnoreCase("lock", action)) {
				result = getLock();

			} else if (containsIgnoreCase("lock", action)) {
				result = getHello();

			} else if (containsIgnoreCase("treasure", action)) {
				result = getTreasure();
				lastAction = "critters";

			} else if (containsIgnoreCase("quest", action)) {
				result = getQuest();
				lastAction = "critters";

			} else if (containsIgnoreCase("trolls", action)) {
				result = getTrolls();

			} else if (containsIgnoreCase("orcs", action)) {
				result = getOrcs();

			} else if (containsIgnoreCase("goblins", action)) {
				result = getGoblins();

			} else if (containsIgnoreCase("skeleton", action)) {
				result = getSkeletons();

			} else if (containsIgnoreCase("hobgoblins", action)) {
				result = getHobgoblins();

			} else if (containsIgnoreCase("fungi folk", action)) {
				result = getFungiFolk();

			} else if (containsIgnoreCase("rats", action)) {
				result = getRats();

			} else if (containsIgnoreCase("vampire bats", action)) {
				result = getVampireBats();

			} else if (containsIgnoreCase("swarmlings", action)) {
				result = getSwarmlings();

			} else if (containsIgnoreCase("centipedes", action)) {
				result = getCentipedes();

			} else if (containsIgnoreCase("vampire frogs", action)) {
				result = getVampireFrogs();

			} else if (containsIgnoreCase("skeletal rats", action)) {
				result = getSkeletalRats();
				

			} else if (containsIgnoreCase("vermin", action)) {
				result = getVermin();
				lastAction = "critter";

			} else if (containsIgnoreCase("minion", action)) {
				result = getMinion();
				lastAction = "critter";

			} else if (containsIgnoreCase("boss", action)) {
				result = getBoss(true);
				lastAction = "critter";

			} else if (containsIgnoreCase("getRoom", action)) {
				result = doRoom();
				result = result + getLock();
				if (containsIgnoreCase("empty", result))
					System.out.println("room empty. you can do a search now.");

			} else if (containsIgnoreCase("getCorridor", action)) {
				result = doCorridor();
				if (containsIgnoreCase("empty", result))
					System.out.println("corridor empty. you can do a search now.");
			
			} else if (containsIgnoreCase("roomlist", action)) {
				result = showRoomList();
				lastAction = "critters";
				

			} else if (containsIgnoreCase("search", action)) {

				if (lastAction.contentEquals("room") || lastAction.contentEquals("corridor")) {
					result = getSearch(lastAction);
				} else {
					System.out.println("not sure how you got to search. Try again.");
					result = "bad action in search";
				}
				lastAction = "";
			} else
			{
				System.out.println("action not in list. try again.");
				result ="";
			}
			

			// System.out.printf("doIt(): lastAction=%s result=%s \n", lastAction, result);

		}

	}

	public boolean containsIgnoreCase(String str, String subString) {
		return str.toLowerCase().contains(subString.toLowerCase());
	}

	private void exit(int i) {
		// TODO Auto-generated method stub

	}

	String getMapPiece() {
		lastAction = "map";
		int room = (pd.roll() * 10) + pd.roll();
		boolean corridor = isCorridor(room);
		String output = String.format("You drew %s piece: %d \n", isCorridor(room) ? "corridor" : "room", room);
		System.out.printf(output);
		myList.add(output);
		return output;
	}
	
	ArrayList<String> myList = new ArrayList<String>();
	
	String showRoomList() {
	
		   /* Advanced For Loop*/ 		
	      System.out.println("==========");
	      int ii = 1;
	      for (String str : myList) { 		      
	           System.out.print(Integer.toString(ii++)+":"+str); 		
	      }
	      System.out.println("==========");
	      
		return "\n";
	}
	
	
	String getLock() {

		//lastAction = "lock";
		
		String output ="";
		if (pd.roll() > 3) 
			output = String.format(" (lock lvl:%d)\n", pd.roll() );


		System.out.printf(output);
		
		return output;
	}

	private String getHello() {
		lastAction = "hello";
		
		String output = String.format("Hello to you stranger:%d\n", pd.roll() );
		System.out.printf(output);
		
		return output;
	}
	
	
	String r1() {

		lastAction = "roll";
		
		String output = String.format("You rolled: %d \n", pd.roll() );
		System.out.printf(output);
		
		return output;
	}
	
	String r2() {

		lastAction = "roll";
		
		String output = String.format("You rolled: %d \n", pd.roll() + pd.roll() );
		System.out.printf(output);
		
		return output;

	}
	String r3() {

		lastAction = "roll";

		String output = String.format("You rolled: %d \n", pd.roll() + pd.roll() + pd.roll() );
		System.out.printf(output);
		
		return output;

	}

	boolean isCorridor(int toCheckValue) {
		int[] corridor = new int[] { 11, 12, 13, 14, 32, 33, 42, 45, 53, 55, 63, 65 };

		for (int element : corridor) {
			if (element == toCheckValue) {
				return true;
			}
		}
		return false;
	}

	String doCorridor() {

		// System.out.println("in doCooridor");

		lastAction = "corridor";

		switch (pd.rollArray(2)) {

		case 2:
			return "Found treasure: " + getTreasure();

		case 3:
			return "Found trap: " + getTrap();

		case 5:
			return "Found special feature: " + getSpecialFeature();

		case 6:
			return "Found vermin: " + getVermin();

		case 7:
			return "Found minion: " + getMinion();

		case 4:
		case 8:
		case 9:
		case 10:
		case 12:
			return "empty";

		case 11:
			return "Found boss:" + getBoss(isFinal);

		}

		return "bad number in coridor";
	}

	String doRoom() {

		lastAction = "room";

		switch (pd.rollArray(2)) {

		case 2:
			return "Found treasure: " + getTreasure();
		case 3:
			return "Found trap: " + getTrap() + "  and treasure:" + getTreasure();
		case 4:
			return "Found special event: " + getSpecialEvent();
		case 5:
			return "Found special feature: " + getSpecialFeature();
		case 6:
			return "Found vermin: " + getVermin();
		case 7:
		case 8:
			return "Found minion: " + getMinion();
		case 9:
			return "empty: " + getEmpty();
		case 10:
			return "Found wierd monsters: " + getWeirdMonsters();
		case 11:
			return "Found boss: " + getBoss(isFinal);
		case 12:
			return "Found dragons lair: " + getDragonsLair();
		}
		return "nothing in room";

	}

	String getTreasure() {
		int ii = 0;

		switch (pd.roll()) {
		case 1:
			ii = getGold(1);
			//System.out.printf("Found %d gold", pd.roll());
			return "Found:"+ Integer.toString(ii) + " gold\n";

		case 2:
			ii = getGold(2);
			//System.out.printf("Found %d gold", pd.roll());
			return "Found:"+ Integer.toString(ii) + " gold\n";

		case 3:
			return "Found " + getScroll();

		case 4:
			return "Found " + getGem();

		case 5:
			return "Found " + getJewelry();

		case 6:
			return "Found " + getMagicItem();

		default:

		}
		return "getTreasure default Value";

	}

	private String getJewelry() {

		// One item of jewelry worth 3d6 x 10 gold pieces

		int ii = getGold(3) * 10;
		return "Found " + Integer.toString(ii) + " jewelry";

	}

	private String getGem() {

		int ii = getGold(2) * 5;
		return "Found " + Integer.toString(ii) + " gem";

	}

	private String getTrap() {

		String[] myScrolls = new String[] { "0", "dart lvl2 random char", "posion gas lvl3 all char",
				"trapdoor lvl4 under character lading", "bear trap lvl4 hitting char leading",
				"spear coming out of wall lvl 5 two leading chars", "stone blcok lvl 5, last char" };
		return "Found " + myScrolls[pd.roll()] + " (page 59)";
	}

	private String getScroll() {
		// TODO Auto-generated method stub
		String[] myScrolls = new String[] {"0", "Fireball", "Blessing", "lightening Bolt", "Sleep", "Escape", "Protect" };
		return "Found " + myScrolls[pd.roll()] + " page 47 & 74";
	}

	private String getMagicItem() {
		// TODO Auto-generated method stub
		String[] myMagicItem = new String[] { "Wand of Sleep", "Ring of Teleportation", "Fools Gold", "Magic Weapon",
				"Potion of Healing", "Fireball Staff" };
		return "Found " + myMagicItem[pd.roll()] + " page 34 & 73";
	}

	private int getGold(Integer quan) {

		// System.out.printf("in showGold()");
		int sum = 0;
		for (int ii = 0; ii < quan; ii++) {
			sum += pd.roll();
		}
		// System.out.printf("in getGold(): rolled %d gold\n", sum);
		return sum;
	}

	private String getVermin() {
		// TODO Auto-generated method stub
		String[] myScrolls = new String[] { "0", "3d6 rats", "3d6 vampire bats", "2d6 goblin swarmslings",
				"d6 giant centepedes", "d6 vampire frogs", "2d6 skeletal rats", "" };
		return " Found " + myScrolls[pd.roll()] + " on page 35 & 74";
	}

	private String getMinion() {
		// TODO Auto-generated method stub
		String[] myScrolls = new String[] { "0", "d6+2 skels or d6 Zombies (50% each)", "d6+3 goblins", "d6 hobgob",
				"d6+1 orcs", "d3 trolls", "2d6 fungi folk" };
		return " Found " + myScrolls[pd.roll()] + " on page 74";
	}	
	
	private String getQuest() {
		// TODO Auto-generated method stub
		String[] myScrolls = new String[] { "0", "Bring me his head! The creature asks the party to kill a boss monster.",
				"Bring me Gold! To complete the quest, the party must bring d6 x 50\r\n" + 
				"worth of treasure to this room.",
				"I want him alive! As 1, above, but the party must subdue the boss, tie\r\n" + 
				"him up with a rope, and take him to the creature’s room to complete\r\n" + 
				"the quest.",
				"Bring me that! Roll on the magic items table to determine what the\r\n" + 
				"object is.",
				"Let peace be your way! To complete the quest, the party must\r\n" + 
				"complete at least three encounters in the adventure in a non violent\r\n" + 
				"way.",
				"Slay all the monsters! To complete the quest, all the dungeon rooms\r\n" + 
				"must be laid out and all the occupants slain...except",
				"", };
		return " Found " + myScrolls[pd.roll()] + " on page 74";
	}

	String getSpecialEvent() {
		// TODO Auto-generated method stub

		String[] myScrolls = new String[] { "0", "ghost", "wondering monst", "lady ion white", "trap",
				"wandering healer", "wandering alchemist" };

		// TODO Auto-generated method stub
		String result = "";
		switch (pd.roll()) {

		case 0:
		case 1:
		case 3:
		case 5:
		case 6:
			result = " Found Special event:" + myScrolls[pd.roll()] + " on page 73";

		case 2:
			result = " Found Special event: wanderingMonster" + getWanderingMonsters();
			break;

		case 4:
			result = " Found Special event: trap" + getTrap();

		default:
			result = " Nothing from Special event:";
		}

		return result;

	}

	String getSpecialFeature() {
		// TODO Auto-generated method stub
		String[] myScrolls = new String[] { "0", "fountain", "Blessed Temple", "Armor", "Cursed altar", "Statue",
				"Puzzle Room" };
		return " Found " + myScrolls[pd.roll()] + " on page 72";
	}

	String getSearch(String lastAction) {

		// TODO Auto-generated method stub
		String result = "";
		switch (pd.roll()) {
		case 0:
		case 1:
		case 2:
			result = " Found wanderingMonster" + getWanderingMonsters();
			break;

		case 3:
		case 4:
		case 5:
			result = " Searched: really empty";
			break;

		case 6:
			result = " Searched: clue,secret door, or hidden treasure";
			break;

		default:
			result = " Nothing from getSearch";
		}

		return result;
	}

	String getWanderingMonsters() {
		// TODO Auto-generated method stub
		String result = "";
		switch (pd.roll()) {
		case 1:
		case 2:
			result = " Found vermin:" + getVermin();

		case 3:
		case 4:
			result = " Found minion:" + getMinion();
		case 6:
			result = " Found boss:" + getBoss(false);
		case 5:
			result = " Found wierd monster:" + getWeirdMonsters();
		}
		return result;
	}

	String getEmpty() {
		return " Empty. You should probably search it";
	}

	String getEmptyRoomSearch() {
		return " Empty Room Search. You should probably search it";
	}

	String getWeirdMonsters() {

		String[] myScrolls = new String[] { "0", "minotaur", "Iron eater", "chimera", "Catoblepas", "Giant Spider",
				"invisible gremlins" };
		return " Found " + myScrolls[pd.roll()] + " on page 75";
	}

	String getBoss(boolean isFinal2) {

		String[] myScrolls = new String[] { "0", "Mummy", "Orc Brute", "Ogre", "Medusa", "Chaos lord", "Small dragon" };
		return " Found " + myScrolls[pd.roll()] + " on page 75";
	}

	String getDragonsLair() {

		String[] myScrolls = new String[] { "0", "", "", "", "", "", "" };
		return " Found " + myScrolls[pd.roll()];
	}



	String getSkeletons() {
		lastAction = "critters";
		return "\n D6+2 skeletons or d6 zombies (50% chance of each). Level 3 undead."
				+ "\n No treasure. Crushing weapons attack Skeletons at +1. Arrows are at -1"
				+ "\n against both skeletons and zombies. Skeletons and zombies never test" + " morale."
				+ "\n Reactions: always fight to the death.";

	}

	String getGoblins() {

		lastAction = "critters";
		return "\n d6+3 goblins. Level 3, treasure -1. Goblins have a 1 in 6 chance of"
				+ "\n gaining surprise, thus acting before the party. If they do act before the"
				+ "\n party, roll d6 on their reactions table below."
				+ "\n Reactions (d6): 1 flee if outnumbered, 2-3 bribe (5 gp per goblin), 4–6" + " fight.";
	}

	String getHobgoblins() {

		lastAction = "critters";
		return "\n d6 hobgoblins. Level 4, Treasure +1."
				+ "\n Reactions (d6): 1 flee if outnumbered, 2–3 bribe (10 gp per hobgoblin),"
				+ "\n 4–5 fight, 6 fight to the death.";
	}

	String getOrcs() {

		lastAction = "critters";
		return "\n D6+1 orcs. Level 4. Orcs are afraid of magic and must test morale each"
				+ "\n time one or more is killed by a spell. If a spell caused their number to"
				+ "\n drop below 50%, they will test morale at -1. They never have magic"
				+ "\n items in their treasure: treat any rolled magic as d6 x d6 gold pieces" + " instead."
				+ "\n Reactions (d6): 1-2 bribe (10 gp per orc), 3–5 fight, 6 fight to the death.";
	}

	String getTrolls() {
		lastAction = "critters";
		return "\n d3 trolls. Level 5, Treasure: normal. Trolls regenerate, unless killed by a"
				+ "\n spell, or unless a character uses one attack to chop an already killed"
				+ "\n troll to bits. If this does not happen, roll a die for every killed troll on its"
				+ "\n next turn. On a 5 or 6, the troll will come back to life and continue to" + " fight."
				+ "\n Reactions (d6): 1–2 fight, 3–6 fight to the death. If a dwarf is present in"
				+ "\n the party, trolls will automatically fight to the death.";

	}

	String getFungiFolk() {
		lastAction = "critters";
		return "\n 2d6 Fungi Folk. Level 3, Treasure: normal. Any character taking"
				+ "\n damage from the fungi folk must save versus level 3 poison or lose 1"
				+ "\n life. Halflings add their level on this save."
				+ "\n Reactions (d6): 1-2 ask for bribe (d6 gp per fungus), 3–6 fight.";

	}

	String getRats() {
		lastAction = "critters";
		return "\n  3d6 rats Level 1, no treasure. Any character wounded has a 1 in 6"
				+ "\n chance of losing 1 additional life due to an infected wound."
				+ "\n Reactions (d6): 1–3 flee, 4–6 fight";
	}

	String getVampireBats() {

		lastAction = "critters";
		return "\n 3d6 vampire bats, level 1, no treasure. Spells are cast at -1 due to"
				+ "\n their distracting shrieking." + "\n Reactions (d6): 1–3 flee, 4–6 fight";
	}

	String getSwarmlings() {

		lastAction = "critters";
		return "\n 2d6 goblin swarmlings, level 3, treasure -1, morale -1"
				+ "\n Reactions (d6): 1 flee, 2-3 flee if outnumbered, 4 bribe (5 gp x goblin)," + "\n 5–6 fight.";
	}

	String getCentipedes() {

		lastAction = "critters";
		return "\n D6 giant centipedes, level 3, no treasure. Any character wounded"
				+ "\n by a giant centipede must save versus level 2 poison or lose 1" + "\n additional life."
				+ "\n Reactions (d6): 1 flee, 2-3 flee if outnumbered, 4-6 fight.";
	}

	String getVampireFrogs() {

		lastAction = "critters";
		return "\n D6 vampire frogs, level 4, treasure -1."
				+ "\n Reactions (d6): 1 flee, 2-4 fight, 5-6 fight to the death";
	}

	String getSkeletalRats() {
		lastAction = "critters";
		return "\n 2d6 skeletal rats, level 3 undead, no treasure. Crushing weapon"
				+ "\n attacks are at +1 against skeletal rats, but they cannot be attacked" + "\n by bows and slings."
				+ "\n Reactions (d6): 1-2 flee, 3-6 fight";
	}


	
	
	
	
}
