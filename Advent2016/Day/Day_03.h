#pragma once
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

namespace Day_03 {

	class Triangle {
	public:
		Triangle(int _a, int _b, int _c);
		bool isTriangle();

	private:
		int a;
		int b;
		int c;
	};

	class Day_03  {
	private:

		int triangleCount;
		std::string input;
		std::vector<Triangle*> triangles;
		std::vector<int> integers;

	public:
		void ReadFile(std::string fileName);
		void Evaluate();
		void PrepareTask2();
		void Print();
		Day_03();
		~Day_03();

	};
}
