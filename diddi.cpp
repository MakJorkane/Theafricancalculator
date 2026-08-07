#include <iostream> // Idk main stuff
#include <cmath> // For Math
#include <random> // For random stuff


int tosfunction(){
   
    bool thevalue = true;

    std::string tos; // Tos Yes or NO!!!!!!!!!!!!!!

    std::cout << "Welcome to thy calculator, currently inputs will be from the CLI, if you want to perform certain functions eg the mean of a value you just type mean" << '\n';
    std::cout << "Read all the instructions on the paper, do you accept the calculator TOS?  (INPUT Y OR N case sensitive)" << '\n';

    std::cin >> tos;

    while(thevalue){ // Ts boolean
    if (tos == "Y" || tos == "y" || tos == "Yes" || tos == "yes" || tos == "ja" || tos == "Ja"){
        std::cout << ("Good Job");
        thevalue = false;
    }
    else if (tos == "N" || tos == "n" || tos == "No" || tos == "no" || tos == "nee" || tos == "Nee"){ // Bad code could use captilization later and no whitespace but I'm lazy rn
        std::cout << "Ok u cant use the calculator turn me on again if u feel like accepting the TOS";
        return 0;
    }
    else{
        std::cout << "Ok so u need valid inputs" << '\n';
        tosfunction();
    }
}
    std::cout << "This should output";
    userinput();

    return 0;
}


int userinput(){

    int thyrandomnumber;
    int maxvalue;
    int minvalue;

    srand(time(0));

    thyrandomnumber = rand() % (maxvalue - minvalue + 1) + minvalue;
    std::cout << "We are debugging random number" << thyrandomnumber;


    std::string input;

    std::cout << "Time to enter your calc: ";
    std::getline (std::cin, input);  // Main input and we need to take in whitespace

    int tempswitch;

    // Big issue eval value does not exist in c++ because everything is compiled so we need alternative method
    // One method could be grouping a bunch of existing integers and then executing them e.g 234234 * 43243 would group it as group1 * group2 

    switch(tempswitch){
    
    
    case 1:{
        
    }

    case 2:{

    }

    case 3:{

    }

    case 4:{

    }

    case 5:{

    }
   
    }


    if(input.find('*')){ //Might use switches later because its better than 50 elifs
    
    std::cout << "We are now doing multiplicaton";

    }

    else if(input.find('/')){

        std::cout << "We are now doing some division";
    }

        else if(input.find('+')){

        std::cout << "We are now doing some addition";
    }

        else if(input.find('-')){

        std::cout << "We are now doing some subtraction";
    }



    return 0;





}