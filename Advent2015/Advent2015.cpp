// Advent2015.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#include "Day_01.h"
#include "Day_02.h"
#include "Day_03.h"
#include "Day_04.h"
#include "Day_05.h"


int main()
{

	// move to UT
	//Day_05::Word t0("aeiouaeiouaeiou");		// nice
	//Day_05::Word t1("ugknbfddgicrmopn");	// nice
	//Day_05::Word t2("jchzalrnumimnmhp");	// naughty
	//Day_05::Word t3("haegwjzuvuyypxyu");	// naughty
	//Day_05::Word t4("dvszwmarrgswjxmb");	// naughty
	//

	Day_05::Word t0("qjhvhtzxzqqjkmpb");		// nice
	Day_05::Word t1("xxyxx");	// nice
	Day_05::Word t2("uurcxstgmygtbstg");	// naughty
	Day_05::Word t3("ieodomkazucvgmuy");	// naughty
	std::cout << t0.IsNiceAnother() 
		<< "\n 1: " << t1.IsNiceAnother() 
		<< "\n 2: " << t2.IsNiceAnother() 
		<< "\n 3: " << t3.IsNiceAnother() 
		<< std::endl;


	Day_01::Day_01 day01;
	day01.DoMagic();
	day01.PrintOutput();

	Day_02::Day_02 day02;
	day02.DoMagic();
	day02.PrintOutput();

	Day_03::Day_03 day03;
	day03.DoMagic();
	day03.PrintOutput();

	// takes some time
	/*
	Day_04::Day_04 day04;
	day04.DoMagic();
	day04.PrintOutput();
	*/

	Day_05::Day_05 day05;
	day05.DoMagic();
	day05.PrintOutput();
}

