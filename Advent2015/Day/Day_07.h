#pragma once
#include "Day.h"
#include <vector>
#include <map>
#include <memory>

namespace Day_07 {

	enum GateType {
		AND,
		OR,
		RSHIFT,
		LSHIFT,
		NOT,
		INPUT
	};

	class IGate {
	public:
		virtual void process() = 0;
		std::string raw;
		std::string id;
		std::string operandName1, operandName2;
		unsigned short operand1, operand2, output;
		unsigned char missingOperands;
		int processCount;

		inline IGate(const IGate & other) {};
		inline IGate & operator=(const IGate & other) { return *this; };
		bool ready, processed;

		void Initialize();

		void Update(const IGate* other);

		IGate(std::string);
		virtual ~IGate();
	};

	class GateAND : public IGate {
	public:
		GateAND(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	class GateOR : public IGate {
	public:
		GateOR(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	class GateLSHIFT : public IGate {
	public:
		GateLSHIFT(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	class GateRSHIFT : public IGate {
	public:
		GateRSHIFT(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	class GateNOT : public IGate {
	public:
		GateNOT(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	class GateINPUT : public IGate {
	public:
		GateINPUT(std::string _w) : 
			IGate::IGate(_w) {
		};
		// Inherited via Gate
		virtual void process() override;
	};

	static class GateFactory {
		static const int GatesBuilt = 0;
	public:
		static std::unique_ptr<IGate> BuildGate(std::string word);
	};

	class Day_07 : public Day {
	private:
		std::fstream input;
		std::vector<std::unique_ptr<IGate>> gates;

		int output;

		void DoTheMagic();

	public:
		Day_07();
		~Day_07();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
