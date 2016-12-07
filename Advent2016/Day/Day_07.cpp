#include "stdafx.h"
#include "Day_07.h"

Day_07::Day_07::Day_07() 
: expr("(\\[[a-z]+\\])"),
	task1(0),
	task2(0)
{
};

Day_07::Day_07::~Day_07() {
};


bool Day_07::Day_07::IsAbba(std::string& str) {
	for (int i = 0; i < str.size() - 3; ++i) {
		if (str[i] == str[i + 3]
			&& str[i + 1] == str[i + 2]
			&& str[i] != str[i + 1]) {
			return true;
		}
	}
	return false;
}

bool Day_07::Day_07::IsKek(std::string& kek, std::string& eke) {
	for (size_t i = 0; i < kek.size() - 2; ++i) {
		if (kek[i] == kek[i + 2] && kek[i] != kek[i + 1]) {
			for (size_t j = 0; j < eke.size() - 2; ++j) {
				if (kek[i] == eke[j + 1]
					&& kek[i + 1] == eke[j]
					&& eke[j] == eke[j + 2]
					&& eke[j] != eke[j + 1]) {
					return true;
				}
			}
		}
	}
	
	return false;
}

void Day_07::Day_07::Evaluate() {
	std::string wordPart;

	for (auto word : words) {
		bool increment = true;
		wordPart = word;

		ss.str(""); // clear
		std::regex_iterator<std::string::iterator> it(word.begin(), word.end(), expr), end;

		while (it != end) {
			ss << it->str();
			++it;

			wordPart = std::regex_replace(wordPart, expr, "|$2");
		}

		if (IsAbba(ss.str())) {
			increment = false;
		}
		if (increment && IsAbba(word)) {
			++task1;
		}
		if (IsKek(wordPart, ss.str())) {
			++task2;
		}
	}
}

void Day_07::Day_07::Print() {
	std::cout << "Day 07 task1: " << task1 << " task2: " << task2 << std::endl;
}