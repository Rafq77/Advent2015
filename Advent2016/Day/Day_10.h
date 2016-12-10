#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include "Day.h"

namespace Day_10 {

	class Bot {
	public:
		Bot(int _id);
		void GiveValue(int _val);
		void SetRecipents(int _low, int _high);
		void SetOutput(int _out);
		bool IsReady() { return ready; };
		void Done();
		void CheckOutput();
		int low;
		int lowRecipent;
		int high;
		int highRecipent;
		int id;
		int elementCount;
	private:
		void AmITheOne();
		bool ready;
		int output;
		static const int MAX_ELEMENTS = 2;
		static const int KEY_LOW = 17;
		static const int KEY_HIGH = 61;
	};

	static unsigned int task1 = 1;
	static unsigned int task2 = 1;
		
	class Day_10 : public Day::Day {
	private:


		void ExecuteInstruction(std::vector<std::string> instr);
		std::vector<Bot> bots;

	public:
		void Evaluate();
		void Print();
		Day_10();
		~Day_10();
	};

}
