// Advent2015.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#include "Day_01.h"
#include "Day_02.h"
#include "Day_03.h"


int main()
{
	Day_01::Day_01 day01;
	day01.DoMagic();
	day01.PrintOutput();

	Day_02::Day_02 day02;
	day02.DoMagic();
	day02.PrintOutput();

	Day_03::Day_03 day03;
	day03.DoMagic();
	day03.PrintOutput();
}

