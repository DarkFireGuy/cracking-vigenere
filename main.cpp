#include <string>
#include <iostream>
#include <regex>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <chrono>
std::string find_key(std::string text, int n = 2);
// Vigenere
std::string keyStream(std::string text, std::string key);
std::string enc_dec(std::string text, std::string key, int n);
//Friedman
double ioc(std::string text);
int split(std::string, int groups, std::string * splits);
// Chi-Square
double chi_square_statistic(std::string text);
std::string chi_square_bruteforce(std::string , int key_length);
// Tools
bool is_alpha(std::string text);
int frequencies(std::string text, int * freqs);

int main(int argc, char** argv) {
    auto start = std::chrono::high_resolution_clock::now();
    if(argc != 2) {
        std::cout << "ERROR: Expected file name\nUsage: \'vigenere.exe /path/to/cipher.txt\'";
        return 0;
    }
    std::string text {};
    std::string tmp_text {};
    std::ifstream read_file(argv[1]);
    while(std::getline(read_file, tmp_text)) {

        tmp_text.erase(remove_if(tmp_text.begin(), tmp_text.end(), [](char c) { return !isalpha(c); } ), tmp_text.end());
        for(int i=0; i<tmp_text.length(); i++) tmp_text[i] = std::toupper(tmp_text[i]);
        text += tmp_text;

    }
    std::string key = find_key(text);
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "The key has been found:\n" << key << "\nTook " << duration.count() << " milliseconds";

    return 0;

}


std::string find_key(std::string text, int n) {
    std::string *splits = new std::string [n]{};
    split(text, n, splits);
    double avg_IOC{};
    double english_IOC = 0.066;
    for(int i=0; i<n; i++) {
        avg_IOC += ioc(splits[i]);
    }
    avg_IOC /= n;
    double error = std::abs((avg_IOC - english_IOC)) / english_IOC;
    //std::cout << n << " Error: " << error << "\n";
    if(error > 0.1) {
        delete[] splits;
        return find_key(text, n+1);
    }
    else {
        return chi_square_bruteforce(text, n);
    }

}

// Vigenere
std::string keyStream(std::string text, std::string key) {

    int multiple = text.length() / key.length() + 1;
    std::string output; output.reserve(key.length() * multiple);
    for(int i = 0; i < multiple; i++) output.append(key);
    return output.substr(0, text.length());

}
std::string enc_dec(std::string text, std::string key, int n) {

    key = keyStream(text, key);
    std::string output {};
    for(int i=0; i < text.length(); i++) {
        int ord = ((int)(text[i])+((int)(key[i]))*n);
            if(ord < 0) {
                    ord += 26;
            }
        output += (char)(ord%26+65);
    }
    return output;

}
// Friedman
double ioc(std::string text) {
    double sum {};
    int freqs[26]{}; frequencies(text, freqs);
    for(int i=0; i<26; i++) {

        sum += freqs[i] * (freqs[i] - 1);

    }
    return sum / (text.length() * (text.length() - 1));
}
int split(std::string text, int groups, std::string * splits) {
    for(int i=0; i < groups; i++) {
        std::string tmp {};
        for(int j=i; j < text.length(); j+=groups) {
            tmp += text[j];
        }
        *(splits+i) += tmp;

    }
    return 1;
}

// Chi-Square

double chi_square_statistic(std::string text) {
    double expected[26] = {0.0820011,
                           0.0106581,
                           0.0344391,
                           0.0363709,
                           0.124167,
                           0.0235145,
                           0.0181188,
                           0.0350386,
                           0.0768052,
                           0.0019984,
                           0.00393019,
                           0.0448308,
                           0.0281775,
                           0.0764055,
                           0.0714095,
                           0.0203171,
                           0.0009325,
                           0.0668132,
                           0.0706768,
                           0.0969225,
                           0.028777,
                           0.0124567,
                           0.0135225,
                           0.00219824,
                           0.0189182,
                           0.00059};
    int length = text.length();
    int freqs[26] {}; frequencies(text, freqs);
    double chi_square {};
    for(int i=0; i<26; i++) {
        double expect = expected[i] * length;
        chi_square += std::pow(freqs[i] - expect, 2) / expect;
    }
    return chi_square;
}
std::string chi_square_bruteforce(std::string text, int key_length) {
    char key[key_length]{};
    std::string splits[key_length]{};
    split(text, key_length, splits);
    for(int i=0; i<key_length; i++) {
        double min_score = INTMAX_MAX;
        char min_char {};
        for(int j=0; j<26; j++) {
            double current_chi_square = chi_square_statistic(enc_dec(splits[i], std::string(1,(char)('A'+j)),-1));
            if(current_chi_square < min_score) {
                min_char = (char)('A'+j);
                min_score = current_chi_square;
            }
        }
        key[i] = min_char;
    }
    return std::string(key);

}

// Tools

bool is_alpha(std::string text) {

    return std::regex_match(text, std::regex("^[A-Za-z]+$"));

}
int frequencies(std::string text, int * freqs) {
    for(int i=0; i<text.length(); i++) {
        int index = (int)text[i] - 65;
        *(freqs + index) += 1;
    }
    return 1;
}