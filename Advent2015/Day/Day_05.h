#pragma once
#include "Day.h"
#include <regex>
#include <vector>
#include <algorithm>

namespace Day_05 {

	class Word {
	private:
		bool isNice;
		std::string word;

		bool HasDouble();
		bool HasInBetweenDouble();
		bool HasDoublePair();
	public:

		Word(std::string _word) :
			word(_word),
			isNice(false) {
		}

		bool IsNice();
		bool IsNiceAnother();

	};


	class Day_05 : public Day {
	private:
		std::fstream input;
		std::vector<Word> words;
		int niceCount;
		int niceAnotherCount;

	public:
		Day_05();
		~Day_05();

		void CheckIsNice();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
