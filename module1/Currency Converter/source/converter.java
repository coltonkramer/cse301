import java.util.Scanner;
import java.text.DecimalFormat;
//Title: Currency Converter
//Author: Colton Kramer
//Description: Converts 5 common currencies between eachother.
 

public class converter {

		public static void main(String[] args) {

			System.out.println("Welcome to the Currency Converter");
			Scanner input = new Scanner(System.in);
			//Uses scanner to get inputs from the user on which currency to use
			System.out.println("Enter which currency you will be using (USD,EUR,JPY,CNY,RUB)");
			
			String currency1 = input.nextLine();
			System.out.println("Currency is " + currency1.toUpperCase());
			
			//Uses scanner again but gets the dollar amount
			System.out.println("Enter the amount you would like to convert");
			String money = input.nextLine();

			//Gets the currency you want to convert into
			System.out.println("Enter the currency that it will be converted to (USD,EUR,JPY,CNY,RUB)");
			String currency2 = input.nextLine();
			input.close();
			
			//converts the string dollar amount into a double
			double newAmount = Double.parseDouble(money);


			

			String symbol1 = "";
			String symbol2 = "";

			// converts everything into us dollars. also grabs the symbol for the coresponding currency
			switch(currency1.toUpperCase()){
				case "USD":
				symbol1 = "$";
				break;
				case "EUR":
				symbol1 = "€";
				newAmount = newAmount * 1.15871;
				break;
				case "JPY":
				symbol1 = "¥";
				newAmount = newAmount * 0.009;
				break;
				case "CNY":
				symbol1 = "¥";
				newAmount = newAmount * 0.15507;
				break;
				case "RUB":
				symbol1 = "₽";
				newAmount = newAmount * 0.01372;
				break;
			}

			//converts from usd to one of the 4 remaining options
			switch(currency2.toUpperCase()){
				case "USD":
				symbol2 = "$";
				break;
				case "EUR":
				symbol2 = "€";
				newAmount = newAmount * 0.86292;
				break;
				case "JPY":
				symbol2 = "¥";
				newAmount = newAmount * 111.12;
				break;
				case "CNY":
				symbol2 = "¥";
				newAmount = newAmount * 6.44468;
				break;
				case "RUB":
				symbol2 = "₽";
				newAmount = newAmount * 72.8191;
				break;
			
			}

			//Prints a statement saying what you have chosen
			System.out.println("You want to convert " + symbol1 + money + " " + currency1.toUpperCase() + " to " + currency2.toUpperCase());
			
			//Converts the number into decimal format so that it will only display 2 digits after the decimal
			DecimalFormat round = new DecimalFormat("0.00");
			//Saves amount to the roundedNewAmount variable
			String roundedNewAmount = round.format(newAmount);
			System.out.println("*******************************************************************************************************************\n");
			System.out.println("Here is your result:");
			//Prints the result of the conversion along with the original selection
			System.out.println(symbol1 + money + currency1.toUpperCase() +  " = " + symbol2 + roundedNewAmount + currency2.toUpperCase());
			System.out.println("\n*******************************************************************************************************************");
			System.out.println("Thank you for using the Currency Converter. \nHave a nice day!");
			

	}
		
}


	

