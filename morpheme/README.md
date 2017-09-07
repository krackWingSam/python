koNLPy 를 이용한 형태소 분석 실험 코드

koNLPY 내부의 클래스들 (kkma, twitter 등..)을 이용하여 문장을 가져오고 해당 문장을 각각의 형태소로 분류하는 작업을 수행한다

프로젝트에서 분석 소스가 될 문장들은 Jordan(전서규)이 작성한 코드를 활용한다. :  https://github.com/swenginejsk/naverCrawler



* Komoran 실행시에 GC overhead limit exceeded 에러를 볼 수 있다.
 해당 에러는 garbage collector가 과도한 시간을 소비하고 있는경우에 발생한다.
 경우에 따라서 JVM의 메모리를 늘려주는 방법으로 해결 가능.
 하지만 궁극적인 해결책은 되지 못한다.