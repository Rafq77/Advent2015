#include "Day_06.h"

Day_06::Day_06::Day_06() {
	InitializeCommonElements();
};

Day_06::Day_06::~Day_06() {
};

void Day_06::Day_06::SortCommonElements() {
	std::sort(commonElements.begin(), commonElements.end(), [](auto &&a, auto &&b) {
		if (std::get<1>(a) == std::get<1>(b)) {
			return std::get<0>(a) < std::get<0>(b);
		} else {
			return std::get<1>(a) > std::get<1>(b);
		}
	});
}

void Day_06::Day_06::InitializeCommonElements() {
	commonElements.clear();
	for (unsigned char i = 'a'; i <= 'z'; ++i) {
		commonElements.push_back(std::make_tuple(i, 0));
	}
}

void Day_06::Day_06::Evaluate() {
	for (size_t i = 0; i < words[0].size(); ++i) {
		InitializeCommonElements();

		std::for_each(words.begin(), words.end(), [&i, this](auto && w) {
			char c = w[i];
			auto it = std::find_if(commonElements.begin(), commonElements.end(), [&c](auto && elem) { 
				return std::get<0>(elem) == c; 
			});
			std::get<1>(*it)++; 
		});

		SortCommonElements();
		task1 += std::get<0>(commonElements[0]); 
		task2 += std::get<0>(commonElements[commonElements.size() - 1]);
	};
}

void Day_06::Day_06::Print() {
	std::cout << "Day 06 task1: " << task1 << " task2: " << task2 << std::endl;
}