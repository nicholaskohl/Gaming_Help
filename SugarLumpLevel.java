import java.util.HashMap;
import java.util.Scanner;
public class SugarLumpLevel 
{ 

   private HashMap<Integer,Integer> calculatedLumps = new HashMap<>();
   public static void main(String[] args)
   {
      System.out.println("Enter the Level you would like to get the building to");
      Scanner scnr = new Scanner(System.in);
      int BulidLevel = scnr.nextInt();
      System.out.println("It would take " + SugarLumps(BulidLevel, new HashMap<>()) + " sugarLumps to get to level " + BulidLevel);
   }
   public static int SugarLumps(int n, HashMap<Integer,Integer> calculatedLumps)
   {
      if(n == 1)
      {
         return 1; 
      }
      if(n == 2)
      {
         return 3;
      }
      if(calculatedLumps.containsKey(n))
      {
         return calculatedLumps.get(n);
      }
      
      int results = n + SugarLumps(n - 1,calculatedLumps);
      calculatedLumps.put(n,results);
      return results;
     
   }
}
