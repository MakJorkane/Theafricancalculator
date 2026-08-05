#include <iostream>
#include <cmath>

int main(){
   
    bool thevalue = true;

    std::string tos; // Tos Yes or NO!!!!!!!!!!!!!!

    std::cout << "Welcome to thy calculator, currently inputs will be from the CLI, if you want to perform certain functions eg the mean of a value you just type mean" << '\n';
    std::cout << "Read all the instructions on the paper, do you accept the calculator TOS?  (INPUT Y OR N case sensitive)" << '\n';

    std::cin >> tos;

    while(thevalue){
    if (tos == "Y" || tos == "y" || tos == "Yes" || tos == "yes"){
        std::cout << ("Good Job");
    }
    else if (tos == "N" || tos == "n" || tos == "No" || tos == "no"){ // Bad code could use captilization later and no whitespace but I'm lazy rn
        std::cout << "Ok u cant use the calculator turn me on again if u feel like accepting the TOS";
        return 0;
    }
    else{
        std::cout << "Ok so u need valid inputs";
        main();
    }
}

    std::cout << "Time to enter your calc: ";
    std::string userinput;  // Main input
    
    std::cin >> userinput;

    if(userinput == "*"){ //Might use switches later because its better than 50 elifs


    }








    return 0;
}