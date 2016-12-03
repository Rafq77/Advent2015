// Advent2016.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "Day\Day_01.h"
#include "Day\Day_03.h"

int main()
{
	Day_01::Day_01 day1;
	day1.ReadFile("Resources/Day_01.txt");
	day1.MoveToPosition();
	day1.WhereAmI();

	Day_03::Day_03 day3;
	day3.ReadFile("Resources/Day_03.txt");
	day3.Evaluate();
	day3.PrepareTask2();
	day3.Evaluate();
	
    return 0;
}

