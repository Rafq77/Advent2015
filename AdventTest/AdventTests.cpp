#include "stdafx.h"
#include "CppUnitTest.h"


#include <iostream>
#include <string>
#include "Day\Day_05.h"

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
	}

	};
}