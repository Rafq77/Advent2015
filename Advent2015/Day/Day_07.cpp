#include "stdafx.h"
#include "Day_07.h"
#include "../Utils/Split.h"
#include <sstream>
#include <regex>

namespace Day_07 {
	Day_07::Day_07() :
		gates() {
	}

	Day_07::~Day_07() {
	}

	void Day_07::DoMagic() {

		input.open("Resources/Day_07.txt", std::ifstream::in);

		if (input.is_open()) {
			std::string word;
			while (true != input.eof()) {
				std::getline(input, word);
				std::unique_ptr<IGate> gate = GateFactory::BuildGate(word);

				/*
					ownership transfer.
					push_back would like to copy,
					but then after function ends original dissapears.
				*/
				gates.push_back(std::move(gate));
			}
			input.close();
		}

		DoTheMagic();

	}

	void Day_07::PrintOutput() {

		int count = std::count_if(gates.begin(), gates.end(), [&](std::unique_ptr<IGate>& g) { return g->processCount != 1; });

		std::cout << "07. Output is " << output << " Gates that have been processed multiple times " << count << std::endl;
	}

	void Day_07::DoTheMagic() {
		int processed = 1;
		int total = gates.size();
		while (total > processed) {

			for (auto &i : gates) {

				// emulate // simulate
				if (true == i->ready) {
					i->process();
				}

				// update outputs
				if (true == i->processed) {

					// second loop
					for (auto &j : gates) {
						// find those "not ready" with missing operands
						if (false == j->ready && j->missingOperands != 0) {
							j->Update(i.get());
						}
					}
				}
			}

			processed = std::count_if(gates.begin(), gates.end(),
				[](std::unique_ptr<IGate>& gate) { return gate->processed; });

			// Debug output:
			//std::cout << "\t" << processed << std::endl;
		}
		

		for (auto &i : gates) {
			if (i->id == "a") {
				output = i->output;
			}
		}
	}

	void GateAND::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = operand1 & operand2;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << operand1 << " & " << operand2 << " -> " << output << std::endl;
		}
	}
	void GateOR::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = operand1 | operand2;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << operand1 << " | " << operand2 << " -> " << output << std::endl;
		}
	}
	void GateLSHIFT::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = operand1 << operand2;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << operand1 << " << " << operand2 << " -> " << output << std::endl;
		}
	}
	void GateRSHIFT::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = operand1 >> operand2;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << operand1 << " >> " << operand2 << " -> " << output << std::endl;
		}
	}
	void GateNOT::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = ~operand1;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << " ~" << operand1 << " -> " << output << std::endl;
		}
	}
	void GateINPUT::process() {
		if (missingOperands == 0
			&& processed == false
			&& ready == true) {

			output = operand1;
			processed = true;
			ready = false;

			// Debug
			++processCount;
			std::cout << "\t" << operand1 << " -> " << output << std::endl;
		}
	}

	std::unique_ptr<IGate> GateFactory::BuildGate(std::string word) {
		std::unique_ptr<IGate> ptr;

		static std::regex patternKeyword = std::regex("[A-Z]+");
		std::smatch match;

		if (std::regex_search(word, match, patternKeyword)) {
			std::string m = match[0];
			if (m == "OR") {
				ptr.reset(new GateOR(word));
			} else if (m == "AND") {
				ptr.reset(new GateAND(word));
			} else if (m == "NOT") {
				ptr.reset(new GateNOT(word));
			} else if (m == "LSHIFT") {
				ptr.reset(new GateLSHIFT(word));
			} else if (m == "RSHIFT") {
				ptr.reset(new GateRSHIFT(word));
			}
		} else {
			ptr.reset(new GateINPUT(word));
		}

		ptr->Initialize();
		return ptr;
	}

	IGate::IGate(std::string _raw) :
		id(""),
		operandName1(""),
		operandName2(""),
		operand1(0),
		operand2(0),
		output(0),
		missingOperands(0xFF),
		processCount(0),
		ready(false),
		processed(false),
		raw(_raw) {
	}

	IGate::~IGate() {
	}

	void IGate::Initialize() {
		size_t pos = raw.find(" -> ");
		std::string lValue = raw.substr(0, pos);
		size_t posEnd = pos + 4;
		size_t firstSpace = 0, secondSpace = 0;

		id = raw.substr(posEnd, raw.size() - posEnd);
		int countSpaces = std::count(lValue.begin(), lValue.end(), ' ');

		switch (countSpaces) {
		case 0: // INPUT
			operandName1 = lValue;
			try {
				operand1 = std::stoi(lValue, nullptr);
				missingOperands = 0;
				ready = true;
			} catch (const std::invalid_argument& ia) {
				std::cout << "Something went wrong " << ia.what() << std::endl;
				ready = false;
				missingOperands = 1;
			}
			break;
		case 1: // NOT
			firstSpace = raw.find(' ', 0);
			operandName1 = raw.substr(firstSpace + 1, pos - firstSpace - 1);
			missingOperands = 1;
			break;
		case 2: // xSHIFT OR AND
			firstSpace = raw.find(' ', 0);
			operandName1 = raw.substr(0, firstSpace);
			secondSpace = raw.find(' ', firstSpace + 1);
			operandName2 = raw.substr(secondSpace + 1, pos - secondSpace - 1);

			if (raw.find("SHIFT") != std::string::npos) {
				missingOperands = 1;
				operand2 = std::stoi(operandName2, nullptr);
			} else {
				missingOperands = 2;
			}

			if (raw.substr(0, 5) == "1 AND") {
				operand1 = 0xFFFF;
				--missingOperands;
			}

			break;
		default:
			break;
		}
	}

	void IGate::Update(const IGate* other) {
		std::string _id = other->id;
		unsigned short _output = other->output;

		if (operandName1 == _id) {
			operand1 = _output;
			--missingOperands;
		}

		if (operandName2 == _id) {
			operand2 = _output;
			--missingOperands;
		}

		if (missingOperands == 0) {
			ready = true;
		}
	}
}
