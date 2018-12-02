#pragma once
#include "./Day.hpp"

class Day_01 : public Day
{
public:

	Day_01()
	{
	}

	~Day_01()
	{
	}

	void solve()
	{
		std::string fileName = "./Resources/Day_01.txt";

		long int sum = 0;

		// 540
		// 73056

		// part 1
		auto x = this->readInput<int>(fileName);
		std::cout << "Sumo of all el.= " << std::accumulate(x.begin(), x.end(), 0) << '\n';

		// part 2
		auto intVector = this->readInput<int>(fileName);

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
	}
};

