cmake_minimum_required(VERSION 4.1)
project(SWEA)

set(CMAKE_CXX_STANDARD 14)

add_executable(SWEA
        main.cpp)
# input.txt 파일을 빌드 결과물이 생성되는 곳으로 복사해줍니다.
configure_file(input.txt input.txt COPYONLY)