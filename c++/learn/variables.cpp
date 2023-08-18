#include <iostream>
#include <cmath>

using namespace std;

int main() {
  string name = "Deadalus";    // two ways of definig variables; variable types always need to be defined
  int age;    // creates variable without defing its content
  age = 2863;
  cout <<"Hi "<<name<<". You are "<<age<<" years old"<<endl;

  // data types
  char character = 'A'; // can store one character; Use ''!!!!!!
  string stringx = "string";
  int intiger = 8;
  float floatx = 0.1245; // not that common in c++ - use double instead
  double doublex = 0.21251545; // can store more decimal places than float
  bool boolean = true; // syntax!

  // strings
  cout <<"lol\n"<<endl; // \n works (new line)

  string text = "Y like trainsI";
  cout <<text.length()<<endl; // nearly like in python; lentg>th< !!! u stupid
  cout <<text[0]<<endl; // like python
  text[0] = 'I'; // '' because of single character

  cout <<text.find("like")<<endl; // can find stuff
  cout <<text.find('I',10)<<endl; // looks for I after 10 digit -> so its 13

  cout <<text.substr(7,5); // grabs parts of strings; 7 = place to start 5 = amout of letters to take

  //numbers
  cout << 5+5 <<endl;
  cout << 5-5 <<endl;
  cout << 5*5 <<endl;
  cout << 5/5 <<endl;
  cout << 5%3 <<endl;

  cout << 5+5*2 <<endl;
  cout << (5+5)*2 <<endl;

  double num = 5.5;
  num ++; // adds 1
  num --; // suptreact 1

  num += 2;
  num -= 2;
  num *= 2;
  num /= 2;

  cout << 10/3 <<endl; // two intigers output intiger so 10/3 = 3
  cout <<10.0/3.0 <<endl; // two decimals (float or double) output decimal so 10.0/3.0 = 3.333333

  // with cmath module (# includle <cmath>)
  cout << pow(3,2) <<endl; // 3 to the power of 2
  cout << sqrt(30) <<endl; // square root
  cout << round(3.1) <<endl; // round to intiger
  cout << floor(3.1) <<endl; // round down
  cout << ceil(3.1) <<endl; // round up
  cout << fmax(3,10) <<endl; // returns the bigger number
  cout << fmin(3,10) <<endl; // returns the smaller number
  return 0;
}
