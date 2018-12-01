#pragma once

#include <string>
#include <vector>
#include <fstream>

#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

template <typename T>
class Day
{
public:

	// reads content of a file (provided in input)
	// returns vector of strings, each vector value corresponds to a line or spearator such as comma or whitespace.
	template <typename T>
	std::vector<T> readInput(std::string fileName)
	{
		std::vector<T> data;
		std::copy(std::istream_iterator<T>(std::ifstream(fileName)), {}, std::back_inserter(data));

		return data;
	}

};
