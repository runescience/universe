package com.jdspub.games;
public class MyNewInfoPacket {
 
    public enum CompanyPacket {
        MONSTER, TREASURE, BOSS, DAMAGE, HIT
    }
 
    CompanyPacket cName;
 
    public MyNewInfoPacket(CompanyPacket cName) {
        this.cName = cName;
    }
 
    public void companyDetails() {
        switch (cName) {
            case MONSTER:
                System.out.println("monsters: Biggest big hairy smelly.");
                break;
 
            case TREASURE:
                System.out.println("Treasure: im rich.");
                break;
 
            case BOSS:
            case DAMAGE:
                System.out.println("bosses do damage: 1st.");
                break;
 
            default:
                System.out.println("DEFAULT: Hit it out of the park");
                break;
        }
    }
 
    public static void main(String[] args) {
    	MyNewInfoPacket ebay = new MyNewInfoPacket(CompanyPacket.MONSTER);
        ebay.companyDetails();
        MyNewInfoPacket paypal = new MyNewInfoPacket(CompanyPacket.TREASURE);
        paypal.companyDetails();
        MyNewInfoPacket google = new MyNewInfoPacket(CompanyPacket.BOSS);
        google.companyDetails();
        MyNewInfoPacket yahoo = new MyNewInfoPacket(CompanyPacket.DAMAGE);
        yahoo.companyDetails();
        MyNewInfoPacket att = new MyNewInfoPacket(CompanyPacket.HIT);
        att.companyDetails();
    }
}