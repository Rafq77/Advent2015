// Advent2015.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#include "Day/Day_01.h"
#include "Day/Day_02.h"
#include "Day/Day_03.h"
#include "Day/Day_04.h"
#include "Day/Day_05.h"
#include "Day/Day_06.h"

int main()
{

	// move to UT
	//Day_05::Word t0("aeiouaeiouaeiou");		// nice
	//Day_05::Word t1("ugknbfddgicrmopn");	// nice
	//Day_05::Word t2("jchzalrnumimnmhp");	// naughty
	//Day_05::Word t3("haegwjzuvuyypxyu");	// naughty
	//Day_05::Word t4("dvszwmarrgswjxmb");	// naughty
	////
	//std::cout << t0.IsNice() 
	//	<< "\n 1: " << t1.IsNice() 
	//	<< "\n 2: " << t2.IsNice() 
	//	<< "\n 3: " << t3.IsNice() 
	//	<< "\n 4: " << t4.IsNice() 
	//	<< std::endl;



	//Day_05::Word t0("qjhvhtzxzqqjkmpb");		// nice
	//Day_05::Word t1("xxyxx");	// nice
	//Day_05::Word t2("uurcxstgmygtbstg");	// naughty
	//Day_05::Word t3("ieodomkazucvgmuy");	// naughty
	//std::cout << t0.IsNiceAnother() 
	//	<< "\n 1: " << t1.IsNiceAnother() 
	//	<< "\n 2: " << t2.IsNiceAnother() 
	//	<< "\n 3: " << t3.IsNiceAnother() 
	//	<< std::endl;


	Day_01::Day_01 day01;
	day01.DoMagic();
	day01.PrintOutput();

	Day_02::Day_02 day02;
	day02.DoMagic();
	day02.PrintOutput();

	Day_03::Day_03 day03;
	day03.DoMagic();
	day03.PrintOutput();

	// takes some time
	//Day_04::Day_04 day04;
	//day04.DoMagic();
	//day04.PrintOutput();

	Day_05::Day_05 day05;
	day05.DoMagic();
	day05.PrintOutput();

	Day_06::Day_06 day06;
	day06.DoMagic();
	day06.PrintOutput();
}

//cheat 
/* 
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int grid[1000][1000];

int get_count() {
	int lights_on = 0;

	for (int x = 0; x < 1000; x++)
		for (int y = 0; y < 1000; y++)
			if (grid[x][y] == 1) ++lights_on;

	return lights_on;
}

void get_coords(istringstream &ss, int &bx, int &by, int &ex, int &ey) {
	string token;
	getline(ss, token, ',');
	bx = stoi(token);
	getline(ss, token, ' ');
	by = stoi(token);
	getline(ss, token, ' ');
	getline(ss, token, ',');
	ex = stoi(token);
	getline(ss, token, ' ');
	ey = stoi(token);
}

void toggle(int begin_x, int begin_y, int end_x, int end_y) {
	for (int x = begin_x; x <= end_x; x++)
		for (int y = begin_y; y <= end_y; y++) {
			if (grid[x][y] == 0) grid[x][y] = 1;
			else grid[x][y] = 0;
		}
}

void turn_off(int begin_x, int begin_y, int end_x, int end_y) {
	for (int x = begin_x; x <= end_x; x++)
		for (int y = begin_y; y <= end_y; y++)
			grid[x][y] = 0;
}

void turn_on(int begin_x, int begin_y, int end_x, int end_y) {
	for (int x = begin_x; x <= end_x; x++)
		for (int y = begin_y; y <= end_y; y++)
			grid[x][y] = 1;
}

int main() {
	string line;
	fstream ifile("Resources/Day_06.txt", ios::in);
	while (getline(ifile, line)) {
		istringstream ss(line);
		string token;
		int begin_x, begin_y, end_x, end_y;

		getline(ss, token, ' ');

		if (token == "toggle") {
			get_coords(ss, begin_x, begin_y, end_x, end_y);
			toggle(begin_x, begin_y, end_x, end_y);
		}
		else {
			getline(ss, token, ' ');
			get_coords(ss, begin_x, begin_y, end_x, end_y);

			if (token == "off") turn_off(begin_x, begin_y, end_x, end_y);
			else turn_on(begin_x, begin_y, end_x, end_y);
		}
	}
	ifile.close();

	int lights_on = get_count();
	cout << "There are " << lights_on << " lights on.\n";

	std::fstream out;
	std::stringstream row("");
	out.open("./Out.txt", std::fstream::out);

		//for (auto& x : map) {
			//for (auto& y : x) {
		for (int x = 0; x < 1000; ++x) {
			row.str("");
			for (int y = 0; y < 1000; ++y) {
				if (true == grid[x][y]) {
					row << "X";
				}
				else {
					row << " ";
				}
			}
			out << row.str() << std::endl;
		}
		out.close();
	return 0;
}
*/