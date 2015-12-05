#include <iostream>
#include <fstream>
#include <string>

#pragma once
class Day {
public:
	virtual void DoMagic() = 0;
	virtual void PrintOutput() = 0;
	Day();
	virtual ~Day();
};

