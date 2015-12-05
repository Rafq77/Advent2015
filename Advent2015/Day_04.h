#pragma once
#include "Day.h"
#include "md5.h"

namespace Day_04 {
	class Day_04 : public Day {
	private: 
		std::string leadingZeros;
		std::string md5sum;
	public:
		int leadingZeroCount;
		long int count;
		std::string input;

		Day_04();
		~Day_04();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
