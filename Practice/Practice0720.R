A_salary <- c(25,80,49,23,52,87,98,65,100,59,83)
A_gender <-as.factor(c('남','남','남','남','남','남','여','여','여','여','남'))
A_hireyears <-c(1,1,5,6,3,3,4,7,4,10,3)
B_salary <- c(45,67,56,87,65,98,76,54,45,69,73)
B_gender <-as.factor(c('여','여','남','남','여','남','여','여','여','여','남'))
B_hireyears <-c(2,3,4,8,5,10,4,5,4,7,7)

mean(A_salary)
median(A_salary)
mean(B_salary)
median(B_salary)

mean(A_salary, na.rm=T)
mean(B_salary, na.rm=T)

range(A_salary)
range(B_salary)

var(A_salary)
var(B_salary)
sd(A_salary)
sd(B_salary)

mean(A_salary, trim=0.1)
mean(B_salary, trim=0.1)

quantile(A_salary)
quantile(A_salary,0.9)
quantile(B_salary)
quantile(B_salary,0.9)

boxplot(A_salary,B_salary,names=c("A회사 연봉","B회사 연봉"))

hist(A_salary, xlab="연봉", ylab="인원수",breaks=4)
hist(B_salary, xlab="연봉", ylab="인원수",breaks=4)

cut_value <- cut(A_salary, breaks=5)
freq <-table(cut_value)
freq


A <-data.frame(gender <-A_gender,
               salary <-A_salary)
B <-data.frame(gender <-B_gender,
               salary <-B_salary)
freqA <-table(A$gender)
freqA

freqB <-table(B$gender)
freqB

prop.table(freqA)
prop.table(freqB)

barplot(freqA, names=c("남","여"), col=c("skyblue","pink"), ylim=c(0,11))
title(main="A사 성비")

barplot(freqB, names=c("남","여"), col=c("skyblue","purple"), ylim=c(0,11))
title(main="B사 성비")

pie(freqA, col=c("skyblue","red"),main="A사")
pie(freqB, col=c("blue","red"), main="B사")

A <-data.frame(salary <-A_salary,
               hireyears <-A_hireyears)
plot(A$salary,A$hireyears, xlab="연봉", ylab="근속연수")

B <-data.frame(salary <-B_salary,
               hireyears <-B_hireyears)
plot(B$salary,B$hireyears, xlab="연봉", ylab="근속연수")

pairs(iris[, 1:4], main="iris data")
cor(iris[,1:4])

cor(A$hireyears,A$salary)
cor(B$hireyears,B$salary)

heatmap(cor(iris[,1:4]))
