#include "stdafx.h"
#include "Day_05.h"
#include <omp.h>

namespace Day_05 {

	Day_05::Day_05() :
		niceCount(0),
		niceAnotherCount(0) {

	}

	Day_05::~Day_05() {
	}

	void Day_05::DoMagic() {

		input.open("Resources/Day_05.txt", std::ifstream::in);

		if (input.is_open()) {
			std::string word;
			while (true != input.eof()) {
				input >> word;
				words.push_back(Word(word));
			}
			input.close();
		}

		CheckIsNice();
	}

	void Day_05::PrintOutput() {
		std::cout << "05. NiceWords " << niceCount << std::endl;
	}

	void Day_05::CheckIsNice() {

		int i = 0;
		int nEnd = words.size();
		int _niceCount = niceCount = 0;
		std::vector<Word> _words = words;

#pragma omp parallel default(none) private(i) shared(_words, _niceCount, nEnd)
		{
#pragma omp for
			for (i = 0; i < nEnd; ++i) {
				//if (words[i].IsNice()) {
				if (words[i].IsNiceAnother()) {
#pragma omp atomic
					++_niceCount;
				};
			}
		}
		niceCount = _niceCount;
	}

	bool Word::IsNice() {

		//[aeiou].*[aeiou].*[aeiou]' | grep '\(.\)\1' | grep -v 'ab\ | cd\ | pq\ | xy' | wc -l
		//It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
		static std::regex patternExclusion = std::regex("(ab|cd|pq|xy)");
		if (std::regex_search(word, patternExclusion)) {
			return false;
		}

		//It contains at least one letter that appears twice in a row, like xx, abcdde(dd), or aabbccdd(aa, bb, cc, or dd).
		// '\1' not recognizable
		//static std::regex patternMatchDouble = std::regex("(.)\1");
		//if (std::regex_search(word, patternMatchDouble)) {

		if (HasDouble()) {
			//It contains at least three vowels(aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
			static std::regex patternMatch3 = std::regex("(.*[aeiou].*){3,}");
			if (std::regex_search(word, patternMatch3)) {
				return true;
			}
		}

		return false;
	}

	bool Word::IsNiceAnother() {
		// It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
		if (HasInBetweenDouble()) {

			// doesnt fucking work
			// It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy(xy) or aabcdefgaa(aa), but not like aaa(aa, but it overlaps).
			//static std::regex patternMatch3 = std::regex("(..).*\1");
			//if (std::regex_search(word, patternMatch3)) {
			if (HasDoublePair()) {
				return true;
			}
		}
		return false;
	}

	// should match 'xx'
	bool Word::HasDouble() {
		for (int i = 1; i < word.size(); ++i) {
			if (word[i] == word[i - 1]) {
				return true;
			}
		}
		return false;
	}

	// should match 'xyx' etc.
	bool Word::HasInBetweenDouble() {
		for (int i = 2; i < word.size(); ++i) {
			if (word[i] == word[i - 2]) {
				return true;
			}
		}
		return false;
	}

	// should match 'xy....xy...' etc.
	bool Word::HasDoublePair() {

		for (int i = 2; i < word.size(); ++i) {
			std::string substring(word.substr(i - 2, 2));

			// taken from rosetta 
			// http://rosettacode.org/wiki/Count_occurrences_of_a_substring#C.2B.2B
			int count = 0;
			for (size_t offset = word.find(substring); offset != std::string::npos;
			offset = word.find(substring, offset + substring.length())) {
				++count;
			}

			if (2 <= count) {
				return true;
			}

		}
		return false;

	}
}
