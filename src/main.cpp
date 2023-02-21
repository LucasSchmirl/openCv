//  made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022
#include <iostream>
#include <opencv2/opencv.hpp> // this header conains all others (openCv)



int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        std::cout << "Usage: " << argv[0] << " <path_to_image>" << std::endl;
        return 1;
    }

    std::string fname = argv[1];

    // load Image with cv::imread(path)
    cv::Mat img = cv::imread(fname, cv::IMREAD_COLOR);

    // check if img contains an image
    if(img.empty()){
        std::cout << "Could not read the image: " << fname << std::endl;
        return 1;
    }

    std::cout << "Loading image from: \"" << fname << "\""<< std::endl;
    // create Window with cv::namedWindow("name", flag) using flag: 0 to make window resizable
    cv::namedWindow("Image: Schaukelbub", 0);
    // insert Image into Window by giving same name
    cv::imshow("Image: Schaukelbub", img);

    std::cout << "Press any key to resize current window to image size." << std::endl;
    // wait for user input (keyboard)
    while(cv::waitKey(0) == 0);


    std::cout << "Press any key to close current window." << std::endl;
    // resize window to image size
    cv::resizeWindow("Image: Schaukelbub", img.size());
    // on some machines 2nd Argument cant be the img.size array. 
    // It has to be ("name", int width, int height)
    // This can be done with: //cv::resizeWindow("name", img.cols, img.rows)

    // wait for user input (keyboard)
    while(cv::waitKey(0) == 0);
    
    std::cout << "End of program.\nClosing all windows..." << std::endl;
    // destroy all windows
    cv::destroyAllWindows();

    return 0;
}