#include "stdafx.h"
#include "Day_04.h"

#include <sstream>

namespace Day_04 {

	/*  KEYS ARE:
		ckczppo
		5 - 117946
		6 - 3938038

		abcdef - 609043
		pqrstuv - 1048970  */
	Day_04::Day_04() :
		count(0) {
		//input = "ckczppo";
		input = "abcdef";
		leadingZeroCount = 5;

		leadingZeros = std::string(leadingZeroCount, '0');
	}

	Day_04::~Day_04() {
	}

	void Day_04::DoMagic() {
		std::string candidate;
		std::stringstream sstream;
		count = 0;

		// openMP?
		while (leadingZeros.compare(md5sum.substr(0,leadingZeroCount)) != 0) {
			sstream.str("");
			sstream << input << std::to_string(++count);

			//calc md5 
			md5sum = md5(sstream.str());
		}
	}

	void Day_04::PrintOutput() {
		std::cout << "04. Zeros at " << count << std::endl;
	}
}
