#include <cstdlib>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
	std::cout << "Calculator App\n";
	float result = 0.0f;
	std::string input;
	char op = '\0';
	while (true) {
		if (op == '\0') std::cout << "Result: " << result << "\n";
		std::cout << "> ";
		std::cin >> input;
		if (input == "exit") {
			std::cout << "Exiting...\n";
			break;
		}
		if (input.length() == 1) {
			bool valid_op = false;
			char c = input[0];
			switch (c) {
				case '+':
				case '-':
				case '*':
				case '/':
					valid_op = true;
					break;
				case 'c':
				case 'C':
					result = 0.0f;
					op = '\0';
					goto after_op;
			}
			if (valid_op) {
				if (op == '\0') op = c;
				else std::cout << "Error: '" << c << "' is not valid after '" << op << "'.\n";
				after_op:
				continue;
			}
		}
		float value;
		try {
			value = std::stof(input);
		} catch (...) {
			std::cout << "Error: Invalid input '" << input << "'.\n";
			continue;
		}
		if (op == '\0') result = value;
		else {
			switch (op) {
				case '+':
					result += value;
					break;
				case '-':
					result -= value;
					break;
				case '*':
					result *= value;
					break;
				case '/':
					if (value == 0.0f) std::cout << "Error: Divide by zero.\n";
					else result /= value;
					break;
			}
			op = '\0';
		}
	}
	return EXIT_SUCCESS;
}
