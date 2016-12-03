#include "stdafx.h"
#include "Day_03.h"


Day_03::Day_03::Day_03() :
	triangleCount(0)
{
};

Day_03::Day_03::~Day_03() {
	for (auto it = triangles.begin(), end = triangles.end(); 
		it != end;
		++it) {
		delete(*it);
	}
};

void Day_03::Day_03::ReadFile(std::string fileName) {
	std::ifstream input;
	std::string one, two, three;
	int a, b, c;

	input.open(fileName, std::ifstream::in);
	if (false == input.is_open()) {
		std::cout << "Can't open file: " << fileName << std::endl;
		return;
	}

	while (true != input.eof()) {
		// read
		input >> one >> two >> three;

		//convert
		a = atoi(one.c_str());
		b = atoi(two.c_str());
		c = atoi(three.c_str());

		// add for first part 
		triangles.push_back(new Triangle(a, b, c));

		// add for 2nd part
		integers.push_back(a);
		integers.push_back(b);
		integers.push_back(c);
	}
	input.close();
}

void Day_03::Day_03::Evaluate() {
	// task 1
	for each (Triangle* triangle in triangles) {
		if (triangle->isTriangle()) {
			++triangleCount;
		}
	}
	Print();
}

void Day_03::Day_03::PrepareTask2() {
	triangleCount = 0;
	
	for each(Triangle* triangle in triangles) {
		delete(triangle);
	}

	// should be empty after deleting all the ptrs? or i have all empty ptrs inside?
	triangles.clear();

	for (size_t i = 0; i < integers.size(); i += 9) {
		triangles.push_back(new Triangle(
			integers[i],
			integers[i+3],
			integers[i+6]
			));

	triangles.push_back(new Triangle(
			integers[i+1],
			integers[i+4],
			integers[i+7]
			));	

	triangles.push_back(new Triangle(
			integers[i+2],
			integers[i+5],
			integers[i+8]
			));
	};
}

void Day_03::Day_03::Print() {
	std::cout << "Found " << triangleCount << " in " << triangles.size() << std::endl;
}

Day_03::Triangle::Triangle(int _a, int _b, int _c)
	: a(_a),
	b(_b),
	c(_c) {
}
bool Day_03::Triangle::isTriangle() {
	bool isTriangle = false;
	if (a < b + c && b < a + c && c < b + a) {
		isTriangle = true;
	}
	return isTriangle;
}
;
