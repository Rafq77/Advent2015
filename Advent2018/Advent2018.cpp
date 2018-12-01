// Advent2018.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <set>
#include <algorithm>
#include "Day\Day.hpp"

int main()
{
	// read input
	Day<int> day01;
	std::string fileName = "./Resources/Day_01.txt";

	long int sum = 0;

	// 540
	// 73056

	// part 1
	auto x = day01.readInput<int>(fileName);
	std::cout << "Sumo of all el.= " << std::accumulate(x.begin(), x.end(), 0) << '\n';

	// part 2
	auto intVector = day01.readInput<int>(fileName);

	bool foundDuplicate = false;
	std::set<long int> set;
	sum = 0;
	while (!foundDuplicate)
	{
		for (auto i : intVector)
		{
			sum += i;
			auto tmp = set.size();
			set.insert(sum);
			if (tmp == set.size())
			{
				foundDuplicate = true;
				std::cout << "Found: " << sum << '\n';
				break;
			}
		}
	}

	
	return 0;
}

