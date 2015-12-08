// Advent2015.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#include "Day/Day_01.h"
#include "Day/Day_02.h"
#include "Day/Day_03.h"
#include "Day/Day_04.h"
#include "Day/Day_05.h"
#include "Day/Day_06.h"
#include "Day/Day_07.h"

int main()
{

	// 138
	// 1771
	Day_01::Day_01 day01;
	day01.DoMagic();
	day01.PrintOutput();

	// 1586300
	// 3737498
	Day_02::Day_02 day02;
	day02.DoMagic();
	day02.PrintOutput();

	// 2081
	// 2341
	Day_03::Day_03 day03;
	day03.DoMagic();
	day03.PrintOutput();

	// 117946
	// 3938038
	// takes some time
	//Day_04::Day_04 day04;
	//day04.DoMagic();
	//day04.PrintOutput();

	// 255
	// 55
	Day_05::Day_05 day05;
	day05.DoMagic();
	day05.PrintOutput();

	// 543903
	// 14687245
	Day_06::Day_06 day06;
	day06.DoMagic();
	day06.PrintOutput();

	// 16076
	// 2797
	Day_07::Day_07 day07;
	day07.DoMagic();
	day07.PrintOutput();
}