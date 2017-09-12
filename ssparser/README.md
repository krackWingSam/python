sam's string parser
txt input 및 output 을 위한 string parser.
구성 - ssparser.py, data_set(input), output

요구사항
    0. 문장 해석을 위한 전처리기
    1. 웹 뉴스를 크롤링하여 만든 [뉴스카테코리 제목] 형식의 문자열 배열을 처리할 수 있어야 한다.
    2. 입력은 txt 파일로 한다.
    3. 결과물은 X 축 데이터(제목) 와 Y 축 데이터(뉴스 카테고리) 가 나와야 한다.                                    //요구사항 제거
    4. Y 축 데이터(뉴스 카테고리) 는 이전의 기록을 유지해야 한다.                                                //요구사항 제거
    5. 만약 새로운 카테고리가 input 데이터로 들어온다면, 기존의 데이터는 유지한 채로 새로운 카테고리만이 추가 되어야 한다,
    6. output data는 data.txt 형태로 출력되며,  카테고리 제목  형태로 줄바꿈을 이용하여 항목을 구분한다.

사용법
    - test.py 참조

파일 설명
    - ssparser.py (sam's string parser)
        *.txt 인풋, 아웃풋을 위한 파일.
        .debug 프로퍼티 : 콘솔에 로그를 확인하기 위한 용도로 사용. default 는 False
        
        .setFilePath(string file path) 
            파일 경로를 설정하는 순간 문자열을 parse하기 시작.
            이전의 데이터를 불러와 데이터를 전처리하고, 파싱한다.

        특수 문자의 제거
            - 문장의 해석을 위해 필요없는 특수문자는 제거한다. (정규표현식 사용)
            - 뉴스의 경우 불필요한 특수문자가 많으므로 해당 문자는 발견할 때마다 "makePrepareData" 함수에서 추가하여야 한다.
            - 현재 정규표현식을 사용하여 나머지 문자는 걸러낸다.
                a-z, A-Z, ㄱ-ㅣ, 가-힣, /


    - slsmaker (sam's sentences maker)
        ssparser 를 통해 출력된 data.txt 를 이용하여 학습용 문장을 랜덤하게 만들기 위한 문장 생성기



    - data_set 폴더
        *.txt input을 위한 폴더


    - output 폴더
        dummy_*.txt, xData.txt, yData.txt, data.txt 를 위한 폴더
        xData, yData 결과물은 가장 마지막의 결과만을 저장하나 dummy 파일의 경우 카테고리 변경의 추적을 위해 일자별로 기록한다.