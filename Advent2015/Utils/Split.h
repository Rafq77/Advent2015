#include "stdafx.h"
#include <string>
#include <sstream>
#include <vector>

#ifndef SPLIT_H
#define SPLIT_H

namespace Utils {

	static std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
		std::stringstream ss(s);
		std::string item;
		while (std::getline(ss, item, delim)) {
			elems.push_back(item);
		}
		return elems;
	}


	static std::vector<std::string> split(const std::string &s, char delim) {
		std::vector<std::string> elems;
		split(s, delim, elems);
		return elems;
	}

}

#endif SPLIT_H