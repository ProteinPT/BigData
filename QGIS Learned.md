## 1. 필드계산기에서 면적 출력($area)

#### /10 ^ 6  => 제곱킬로미터 변환

###  F6 = 속성 테이블



## 2. 면적 구분 속성 추가(기준 범위 설정)

1. 속성 툴바에서 값으로 객체 선택 클릭
2. `area` 에서 기준값 범위 설정 ( >= or <=  등등)

3. 필드 계산기 실행해서 구분할 컬럼명을 가진 필드값 생성 후 출력미리보기를 '값' 입력(필드 유형 `텍스트`)
4. 선택되지 않은 개체는 속성테이블 상단의 반전 누르고 필드 계산기 실행해서 출력 미리보기 '값' 입력



## XYZ타일 추가

- 레이어 추가 Vworld 연결 
- 인증키값 받아와서 해야함. 연결 후 타일세트 탭에서 추가하면 됨.
- EPSG 값은  Vworld 좌표인 3857로 변경해주는 것이 좋음.



## 레이어 생성

- 새 shapefile 레이어 

- 도형 유형 폴리곤
- EPSG 프로젝트 좌표로 설정
- 새로 만들어진 레이어에서 f6 누르고 편집 모드 활성화 시킨 후 새 필드 생성(텍스트형 최대길이 100)
- 디자타이즈 툴바에서 폴리곤 추가 버튼
- 구역 추가 수정 가능



## 결합

- 레이어 추가, 구분자로 분리된 텍스트 추가 버튼
- CSV 파일 불러오기 한 후 인코딩 방식  KOREAN 으로 바꾸고 도형설정에서 없음으로 설정 변경
- 이후 레이어 속성에서 결합탭에서 + 버튼 누르고 결합 레이어 필드 대상필드 설정하고 확인 적용 누르면 
-  CSV 파일과 해당 지도데이터와 데이터 결합됨.



## 지오패키지 생성

#### 첫 번째 방법

- 레이성 생성에서 지오패키지 생성
- NEW_GEOPACKAGE 폴더 저장 후 생성
- 데이터베이스탭에서 DB관리자에 들어가서 지오패키지 오른쪽버튼 후 새연결 후 방금 만든 gpkg 파일 연결 하면 db 연동
- 이 후 상단에 레이어/파일 불러오기 버튼 눌러서 입력탭에 NLPRK_BNDRY 로 설정

#### 두 번째 방법

- 탐색기 창에서 바로 shp 파일을 gpkg로 드래그하면 임포트 됨.





## DEM (Digital Elevation Model)

>  수치표고모델, 실세계 지형 정보 중 건물, 수목, 인공 구조물 등 을 제외한 지형 부분을 표현하는 수치모형

- 보기에서 패널 탭에서 레이어스타일작업에 체크하고 음영기복도(z비율), 단일밴드 유사색상 등등 기능 만져보기



## 위성영상 스타일링

- 똑같이 레이어 스타일작업에서 다중 밴드색상으로 432(자연 부각), 도시부각 등 조합표를 따라 밴드 색상을 지정하면 특징적인 모습을 한 눈에 파악할 수 있다.

- 스트래치 툴바

  위성영상이 갖고있는 최대 최소값이 있을 때, 일정값을 늘려준다



## 토지피복도 스타일링

- 레이어 스타일 작업에서 팔레트/고유값으로 설정하고 분류 버튼 누르기
- 그리고 파일에서 색상표 불러오기 버튼 누르기
- 해당 레이어에서 오른쪽버튼 누르고 심볼에서 화면 왼쪽 하단에서 스타일 불러오기 누르고 
- 확장자 .qml 파일 불러오기
- 스타일 저장하고 타인과 공유할 때 해당 qml 파일을 타인에게 보내주고 보게하면 됨.