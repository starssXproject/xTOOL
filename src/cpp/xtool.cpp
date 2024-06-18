#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <Windows.h>

std::string getExecutablePath() {
    char path[MAX_PATH];
    GetModuleFileNameA(NULL, path, MAX_PATH);
    std::string exePath = std::string(path);
    return exePath.substr(0, exePath.find_last_of("\\/") + 1);
}

void runCommand(const std::string& command) {
    int result = std::system(command.c_str());
    if (result != 0) {
        std::cerr << "Error executing command: " << command << std::endl;
        exit(result);
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1 && std::string(argv[1]) == "install") {
        runCommand("pip install colorama cryptography tqdm");
        return 0;
    }

    std::string scriptDir = getExecutablePath();
    std::string pythonCommand = "python \"" + scriptDir + "src\\main.py\"";

    for (int i = 1; i < argc; ++i) {
        pythonCommand += " \"" + std::string(argv[i]) + "\"";
    }

    runCommand(pythonCommand);
    return 0;
}
