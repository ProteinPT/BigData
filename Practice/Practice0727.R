data<-c(5,6,7,5,5,9,10,3,3,3.5,8,8,7,2,3,3.5,6,6,6,6)
#모평균이 7보다 적은지 단측검정
t.test(data,mu=7, alternative='less')
#대립가설 채택

before <-c(68.12 , 56.94, 57.36, 54.64, 64.33, 48.49, 68.72, 56.19, 61.6, 58.75, 67.31, 49.7, 58.39, 58.08, 65.67, 54.5, 59.14, 55.61 ,60.21 ,62.91)

after <-c( 65.90, 54.79, 57.82, 54.64, 64.84, 47.34, 67.87, 54.58, 60.65, 58.79, 65.71, 48.81, 57.0 ,56.52, 64.13 ,53.94 ,57.22, 55.32, 61.61, 63.22 )

#같은 집단 시점 달리하여 두번 표본 추출 = 대응이표본
#몸무게가 줄어들었는지 한 쪽 방향 차이만 검증 = 단측검정
#단측 검정으로 before 데이터가 더 큰지 검정하므로 greater옵션 사용
t.test(before,after, paired= TRUE,var.equal=TRUE, alternative= "greater")

Seoul<-c(43.12, 40.94, 42.36, 50.64, 50, 43.49, 43.72, 40.19, 46.6, 43.75, 42.31, 44.7, 
         
         43.39, 33.08, 40.67, 49.5, 34.14, 40.61, 35.21, 37.91)

Busan <-c(41.74, 42.35, 40.62, 28.64, 49.64, 40.94, 43.25, 40.3, 56.03, 43.77, 51.3, 44.26, 
          
          42.6, 32.19, 39.72, 49.2, 33.03, 40.45, 36.03, 38.1)
#다른 집단 각각 표본 추출= 독립이표본
#데이터의 값이 크거나 작은 양방향의 차이 확인 = 양측검정
t.test(Seoul,Busan,paired= FALSE, var.equal= FALSE, alternative="two.sided")
#귀무가설 유의하지않음
anova_result <-aov(Sepal.Length ~ Species, data= iris)
summary(anova_result)

cor(Orange$circumference,Orange$age)
#강한 양의 상관관계
plot(Orange$circumference, Orange$age, col="red",pch=19)

cor(iris[,1:4])
#피어슨 상관계수 검정
cor.test(iris$Petal.Length, iris$Petal.Width, method="pearson")
#스피어만 상관계수 검정
cor.test(iris$Petal.Length, iris$Petal.Width, method="spearman")

data(Orange)
head(Orange)

model <- lm(circumference ~ age, Orange)
model
#포뮬러 매개인자: 무엇이 종속변수이고, 무엇이 설명변수인지 표현하는 식
coef(model)

r <-residuals(model)
r[0:4]
#잔차 확인

f <- fitted(model)
r<- residuals(model)
f[0:4] + r[0:4]
Orange[0:4,'circumference']

#잔차제곱합
deviance(model)

#예측
predict.lm(model, newdata= data.frame(age=100))
#predict.lm함수로 나이가 100인 나무 둘레 예측'

summary(model)

height_father <-c(180,172,150,180,177,160,170,165,179,159)

height_mother<- c(160,164,166,188,160,160,171,158,169,159)

height_son <- c( 180,173,163,184,165,165,175,168,179,160)
height <- data.frame(height_father, height_mother, height_son)
head(height)
model <-lm(height_son ~ height_father + height_mother, data= height)
model

#회귀계수 출력
coef(model)
#잔차
r <- residuals(model)
r
r[0:4]
deviance(model)
#잔차제곱합

predict.lm(model, newdata=data.frame(height_father=170, height_mother= 160))
predict.lm(model, newdata=data.frame(height_father=170, height_mother= 160), interval = "confidence")

summary(model)
model <- lm(mpg ~., data= mtcars)
model
new_model <-step(model, direction="both")

model <-lm(mpg ~ wt +qsec+am, data=mtcars)
plot(model)

