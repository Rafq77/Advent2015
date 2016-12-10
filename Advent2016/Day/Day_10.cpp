#include "Day_10.h"

Day_10::Day_10::Day_10() {
	for (int i = 0; i < 210; ++i) {
		bots.push_back(Bot(i));
	}
};

Day_10::Day_10::~Day_10() {
};

Day_10::Bot::Bot(int _id) 
: 
  low(0),
  high(0),
  ready(false),
  elementCount(0),
  lowRecipent(-1),
  highRecipent(-1),
  output(-1),
  id(_id) {
}

void Day_10::Bot::GiveValue(int _val) {
	if (elementCount == 2) {
		std::cout << "cannot give" << std::endl;
		return;
	} else if (elementCount == 0) {
		low = _val;
	} else if (elementCount == 1) {
		if (low != 0) {
			if (low > _val) {
				high = low;
				low = _val;
			} else {
				high = _val;
			}
		} else {
			low = _val;
		}
		ready = true;
	} 
	elementCount++;
	
	AmITheOne();
	CheckOutput();
}

void Day_10::Bot::SetRecipents(int _low, int _high) {
	lowRecipent = _low;
	highRecipent = _high;
}

void Day_10::Bot::SetOutput(int _out) {
	output = _out;
}

void Day_10::Bot::Done() {
	ready = false;
	high = 0;
	low = 0;
	elementCount = 0;
}

void Day_10::Bot::CheckOutput() {
	switch (output) {
	case 0:
	case 1:
	case 2:
		task2 *= low; // little cheat, because i don't compare on which side the output was.
		break;
	default:
		// ignore
		break;
	}
}

void Day_10::Bot::AmITheOne() {
	if (elementCount == 2) {
		if (low == KEY_LOW && high == KEY_HIGH) {
			task1 = id;
		}
	}
}

void Day_10::Day_10::ExecuteInstruction(std::vector<std::string> instr) {
	if (instr.size() < 1)
		return;
	if (instr[0] == "value") {
		int botId = atoi(instr[5].c_str()); 
		auto it = std::find_if(bots.begin(), bots.end(), [&instr,&botId](auto&& bot) {
			return bot.id == botId;
		});
		if (it != bots.end()) {
			(*it).GiveValue(atoi(instr[1].c_str()));
		} else {
			std::cout << "bot not found " << botId << std::endl;
		}
	} else {
		int botId = atoi(instr[1].c_str()); 
		auto it = std::find_if(bots.begin(), bots.end(), [&instr,&botId](auto&& bot) {
			return bot.id == botId;
		});
		if (it != bots.end()) {
			int mul = 1;
			int high = atoi(instr[11].c_str());
			int low = atoi(instr[6].c_str());

			if (instr[5] == "output") {
				(*it).SetOutput(low);
				high = -1;
			}
			if (instr[10] == "output") {
				(*it).SetOutput(high);
				high = -1;
			}

			(*it).SetRecipents(low, high);

		} else {
			std::cout << "bot not found " << botId << std::endl;
		}
	}
}

void Day_10::Day_10::Evaluate() {
	std::string wordPart;
	std::vector<std::string> instruction;

	
	size_t wordCount = 0;
	size_t wordPerInstruction = 12;

	// Initializes the bots
	for (auto& word : words) {
		wordCount++;
		if (word.compare("value") == 0) {
			// different count
			wordCount = 1;
			wordPerInstruction = 6;
		}

		instruction.push_back(word);
		if (wordCount >= wordPerInstruction) {
			wordPerInstruction = 12;
			wordCount = 0;
			ExecuteInstruction(instruction);
			instruction.clear();
		}
	}

	// Propagation of "chips"
	while (std::any_of(bots.begin(), bots.end(), [this](auto && bot) { return bot.IsReady() == true; })) {

		for (auto & bot : bots) {
			if (bot.IsReady()) {
				auto low = std::find_if(bots.begin(), bots.end(), [bot](auto& searchedBot) {
					return searchedBot.id == bot.lowRecipent;
				});
				if (low != bots.end()) {
					(*low).GiveValue(bot.low);
				}
				auto high = std::find_if(bots.begin(), bots.end(), [bot](auto& searchedBot) {
					return searchedBot.id == bot.highRecipent;
				});
				if (high != bots.end()) {
					(*high).GiveValue(bot.high);
				}
				bot.Done();
			}
		}
	}
}

void Day_10::Day_10::Print() {
	std::cout << "Day10: Comparing id:" << task1 << " Mul of 0,1,2:" << task2 << std::endl;
}

