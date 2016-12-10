// Advent2016.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "Day\Day_01.h"
#include "Day\Day_02.h"
#include "Day\Day_03.h"
#include "Day\Day_04.h"
#include "Day\Day_05.h"
#include "Day\Day_06.h"
#include "Day\Day_07.h"
#include "Day\Day_08.h"
#include "Day\Day_10.h"

#include <boost\lambda\lambda.hpp>

static const bool WITH_LONG_RUN = false;

int main()
{
	Day_01::Day_01 day1;
	day1.ReadFile("Resources/Day_01.txt");
	day1.MoveToPosition();
	day1.WhereAmI();

	Day_02::Day_02 day2;
	day2.ReadFile("Resources/Day_02.txt");
	day2.Evaluate();

	Day_03::Day_03 day3;
	day3.ReadFile("Resources/Day_03.txt");
	day3.Evaluate();
	day3.PrepareTask2();
	day3.Evaluate();

	Day_04::Day_04 day4;
	day4.ReadFile("Resources/Day_04.txt");
	day4.Evaluate();
	
	if (WITH_LONG_RUN) {
		Day_05::Day_05 day5;
		day5.Evaluate(); 
	}

	Day_06::Day_06 day6;
	day6.ReadFile("Resources/Day_06.txt");
	day6.Evaluate(); 
	day6.Print();

	if (WITH_LONG_RUN) {
		// std::regex is slow
		Day_07::Day_07 day7;
		day7.ReadFile("Resources/Day_07.txt");
		day7.Evaluate(); 
		day7.Print();
	}

	Day_08::Day_08 day8;
	day8.ReadFile("Resources/Day_08.txt");
	day8.Evaluate(); 
	day8.Print();

	Day_10::Day_10 day10;
	day10.ReadFile("Resources/Day_10.txt");
	day10.Evaluate(); 
	day10.Print();

	using namespace boost::lambda;
	typedef std::istream_iterator<int> in;

	std::for_each(
		in(std::cin), in(), std::cout << (_1 * 3) << " ");

    return 0;
}

