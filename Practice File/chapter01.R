age <-30
age
a
age
class(age)
name <-'Jaeyenog'
name
class(name)
is_effective <-TRUE
is_effective
class(is_effective)
sido <-factor('서울',c('서울','부산','제주'))
sido
class(sido)
level(sido)
a <- NULL
jumsu <-c(NA,90,100)
class(jumsu)
10/0
0/0

vector
students_age <-c(11,13,18,23,25)
length(students_age)
students_age[2]
class(students_age)
data <-seq(1,10,by= 2)
data
data1 <-seq(1,10)
data1
data2 <-c(1:10)
data2
data3 <-rep(1:3,each =3)
data3
data4 <-rep(1:3,each =4)
data4
data5 <-rep(1:5,times =5)
data5

var1 <-c(1,2,3,4,5,6)
x1 <-matrix(var1,nrow=2,ncol=3)
x1

x2 <-matrix(var1,ncol=2)
x2
x1 <- rbind(x1,c(10,10))
x1
var2 <- c(1:12)
var2
x3 <-matrix(var2,ncol= 4)
x3
x3 <- rbind(x3,c(10))
x3
x3 <- cbind(x3,c(10))
x3

no <-c(1:10)
age <- seq(10,100,by=10)
gender <-c('m','m','m','f','f','f','m','f','m','f')
students <-data.frame(no,age,gender)
students
colnames(students) <-c('순번','나이','성별')
students
colnames(students) <-c('no','age','gender')
students
students[,1]
students[,'gender']
students[3,1]
rownames(students) <-c('a','b','c','d','e','f','g','h','i','j')
students
students$name <-c('감','김','이','박','나','잔','조','강','장','전')
students

-----
#다차원 배열 만들기
var1 <- c(1:12)
arr1 <-array(var1,dim=c(2,2,3))
arr1
arr2 <-array(var1,dim=c(12))
arr2
arr3 <-array(var1,dim=c(6,2))
arr3
arr4 <-array(var1, dim=c(2,2,3,1))
arr4

v_data <-c("02-111-2222","01022233333")
m_data <- matrix(c(21:26),nrow=2)
a_data <-array(c(31:36),dim=c(2,2,2))
d_data <- data.frame(address=c('seoul','busan'),
                     name=c("Lee","Kim"),stringsAsFactors = F
                     )
list_data <-list(name="길동",
                 tel=v_data,
                 score1=m_data,
                 score2=a_data,
                 friends=d_data)
list_data
list_data$name
list_data[1]
n=20
n== 10|20|30
n %in%(c(10,20,30))
score_1 <-c(10,20)
score_1 +2
score_1
socre_1 <-score_1 +2
socre_1

score <-c(10,20)
score +2
score
score <-c(score+2)
score

sum_score <-c(score +score_1)
sum_Score

score1 <- c(100,200,300,400)
score2 <- c(90,91)
sum_score1<-score1+score2
sum_score1
diff <- score1 -score2
diff

score3 <-95
if(score3>=80){
  print("성공")
}
score3

score <-86
if(score >=91) {
  print("A")
}else{
  print("B")
}


for(num in (1:3)) {
  print(num)
}

for(num in(1:5)) {
  if(num%%2 ==0)  #1~5를 2로 나눈 나머지가 0이냐?
    print(paste(num,"짝수")) # paste()함수 이어붙여서 돌려줌
  else
    print(paste(num,"홀수"))
}

calculator <-function(num1, op, num2) {
  result<- 0
  if(op =="+") {
    result <- num1+num2
  } else if(op =="-"){
    result <- num1-num2
  } else if(op =="*"){
    result <- num1*num2
  } else if(op =="/"){
    result <- num1/num2
  }
  return(result)
}
n <-calculator(1,"+",89)
n
n <- calculator(169,"/",13)
n

#---------------------

install.packages('data.table')
tail(Orange)
install.packages('openxlsx')
library(openxlsx)

#---------------------
Orange[1]
Orange[1:3]
Orange[Orange$age==118,]
Orange[Orange$age %in% c(118,484),]
Orange[Orange$age >= 1372,]

Orange[,-c(1,3)]
Orange

aggregate(circumference ~Tree,Orange,mean)

#-------------------
stu1 <-data.frame(no=c(1,2,3), midterm= c(100,90,80))
stu2 <-data.frame(no=c(1,2,3), midterm= c(100,90,80))
stu3 <-data.frame(no=c(1,2,3), midterm= c(100,90,80))
stu4 <-data.frame(no=c(1,2,3), midterm= c(100,90,80))
         
cbind(stu1,stu2)         
rbind(stu1,stu4)                  

merge(stu1,stu3, all=TRUE)
