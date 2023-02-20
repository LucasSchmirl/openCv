//  made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

#include <iostream>
#include <opencv2/opencv.hpp>


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

    if(img.empty()){
        std::cout << "Could not read the image: " << fname << std::endl;
        return 1;
    }

    // create Window with cv::namedWindow using flag 1 to make resizable
    cv::namedWindow("Image: Schaukelbub", 0);
    // insert Image into Window by giving same name
    cv::imshow("Image: Schaukelbub", img);


    while(cv::waitKey(0) == 0);
    
    cv::resizeWindow("Image: Schaukelbub", img.size());
    
    while(cv::waitKey(0) == 0);
    
    // cv::destroyAllWindows();

    return 0;
}