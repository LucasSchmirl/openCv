//  made by Lucas Schmirl 25.02.2022,	last edit: 25.02.2022
#include <iostream>
#include <opencv2/opencv.hpp>


// shows product, rows, cols
void showImgInfo(cv::Mat img)
{
    std::cout << "Image size: " << img.size << " = " << img.rows * img.cols << std::endl;
}
void endRoutine()
{
    std::cout << "Press any key to close current window." << std::endl;
    // wait for user input (keyboard)
    cv::waitKey(0);
    
    std::cout << "End of program.\nClosing all windows..." << std::endl;
    // destroy all windows
    cv::destroyAllWindows();
}





int main(int argc, char* argv[])
{
    if (argc != 2) { std::cout << "Usage: " << argv[0] << " <path_to_image>" << std::endl; return 1; }
    std::string fname = argv[1];


    cv::Mat img = cv::imread(fname, cv::IMREAD_COLOR);
    if(img.empty()){ std::cout << "Could not read the image: " << fname << std::endl; return 1; }


    cv::namedWindow("Input-image:", 0);
    cv::imshow("Input-image:", img);
    cv::resizeWindow("Input-image:", img.size());
    
    showImgInfo(img);

/*
/// Denoising Image
    cv::Mat output;
    float filterStrength = 50.0;     // 3    h           // 0-100
    float colorFilterStrengh = 55.0; // 10   color_h     // 0-100
    int templateSize = 5;            // 7    template window size: should be odd // 1-imageSize
    int kernelSize = 19;             // 21   search window size: should be odd   // templateWindowSize-imageSize

    cv::fastNlMeansDenoisingColored(img, output, filterStrength, colorFilterStrengh, templateSize, kernelSize);

    cv::namedWindow("Denoised-image", 0);
    cv::imshow("Denoised-image", output);
    cv::resizeWindow("Denoised-image", output.size());
////
*/

    endRoutine();

    return 0;
}




