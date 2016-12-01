// Advent2016.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "Day\Day_01.h"
//#include "Day_01.h"

int main()
{
	Day_01::Day_01 day1;
	day1.ReadFile("Resources/Day_01.txt");
	day1.MoveToPosition();
	day1.WhereAmI();
	
    return 0;
}

