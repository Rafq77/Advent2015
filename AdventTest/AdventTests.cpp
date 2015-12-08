#include "stdafx.h"
#include "CppUnitTest.h"


#include <iostream>
#include <string>
#include "Day\Day_05.h"
#include "Day\Day_07.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace AdventTest {
	TEST_CLASS(UnitTest1) {
public:

	TEST_METHOD(Day05) {
		//Day_05::Word t0("aeiouaeiouaeiiou");	// nice
		Day_05::Word t1("ugknbfddgicrmopn");	// nice
		Day_05::Word t2("jchzalrnumimnmhp");	// naughty
		Day_05::Word t3("haegwjzuvuyypxyu");	// naughty
		Day_05::Word t4("dvszwmarrgswjxmb");	// naughty

		//Assert::IsTrue(t0.IsNice());
		Assert::IsTrue(t1.IsNice());
		Assert::IsFalse(t2.IsNice());
		Assert::IsFalse(t3.IsNice());
		Assert::IsFalse(t4.IsNice());

		Day_05::Word a0("qjhvhtzxzqqjkmpb");		// nice
		Day_05::Word a1("xxyxx");					// nice
		Day_05::Word a2("uurcxstgmygtbstg");	// naughty
		Day_05::Word a3("ieodomkazucvgmuy");	// naughty

		Assert::IsTrue(a0.IsNiceAnother());
		Assert::IsTrue(a1.IsNiceAnother());
		Assert::IsFalse(a2.IsNiceAnother());
		Assert::IsFalse(a3.IsNiceAnother());
	}

	TEST_METHOD(Day07) {

		std::unique_ptr<Day_07::IGate> ptr;
		std::vector<std::unique_ptr<Day_07::IGate>> vec;

		ptr = Day_07::GateFactory::BuildGate("123 -> x");					// input
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("456 -> y");					// input
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("x AND y -> d");				// and2
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("x OR y -> e");				// or 2
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("x LSHIFT 2 -> f");			// lshift 1
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("y RSHIFT 2 -> g");			// lshift 1
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("NOT x -> h");					// not 1
		vec.push_back(std::move(ptr));

		ptr = Day_07::GateFactory::BuildGate("NOT y -> i");					// not 1
		vec.push_back(std::move(ptr));


		// while all are not done
		int processed = 1;
		while (8 > processed) {

			processed = std::count_if(vec.begin(), vec.end(),
				[](std::unique_ptr<Day_07::IGate>& gate) { return gate->processed; });

			for (auto &i : vec) {

				// emulate // simulate
				if (true == i->ready) {
					i->process();
				}

				// update outputs
				if (true == i->processed) {

					// second loop
					for (auto &j : vec) {
						// find those "not ready" with missing operands
						if (false == j->ready) {
							j->Update(i.get());
						}
					}
				}
			}

			Assert::IsTrue(vec[0]->output == 123);
			Assert::IsTrue(vec[1]->output == 456);
			Assert::IsTrue(vec[2]->output == 72);
			Assert::IsTrue(vec[3]->output == 507);
			Assert::IsTrue(vec[4]->output == 492);
			Assert::IsTrue(vec[5]->output == 114);
			Assert::IsTrue(vec[6]->output == 65412);
			Assert::IsTrue(vec[7]->output == 65079);

			processed = std::count_if(vec.begin(), vec.end(),
				[](std::unique_ptr<Day_07::IGate>& gate) { return gate->processed; });
		}
	}

	};
}