########################
### Install Packages ###
########################

packages <- c("magrittr","httpgd","mFilter","BCDating","rio","timetk","pdftools","textdata","tm",
"tidytext","dplyr","tidyverse","tidyr","ggplot2","readr","readxl","forecast","zoo","lubridate",
"ipeadatar","sidrar","GetBCBData","PNADcIBGE","survey","dygraphs","tseries","quantmod",
"Quandl","discreteRV","aTSA","fGarch","fUnitRoots","vars","MTS","seasonal","stats","nortest",
"scales","urca","dlm","seasonalview","stringr","fma","languageserver","PerformanceAnalytics",
"jsonlite","purrr","curl)")

packages_install <- packages [!packages %in% installed.packages()[,"Package"]]
if(length(packages_install) > 0)
{install.packages(packages_install)} else {message("Todos os pacotes já estão instalados.")}

#####################
### Load Packages ### 
#####################

lapply(packages, library, character.only = TRUE)

#################
### AUTOARIMA ###
#################

dados <- gbcbd_get_series(id = 4385, first.date = "1990-01-01", last.date = Sys.Date())
View(dados)
dygraph(dados, main = "PIB mensal em dólares - US$ (milhões)") %>% dyRangeSelector()

# Criando série
dados_x <- dados$"value"
serie <- ts(dados_x, frequency = 12, star= c(1990))
title("PIB mensal em dólares - US$ (milhões)")
plot(serie)

# Examinar a existência de tendência e/ou sazonalidade nos dados

# Gráfico
decomp <- stl(dados, "periodic")
colnames(decomp$time.series) = c("sazonalidade","tendência","restante")
plot(decomp)

# Teste 
fit <- tbats(dados)
seasonal <- !is.null(fit$seasonal)
seasonal

fit <- tbats(dados)
trend <- !is.null(fit$trend)
trend

# Diminuir o impacto de outliers (interpolação)
serie_suv <- tsclean(serie, replace.missing = TRUE)
plot(serie)
lines(serie_suv, col = "green")

# Estabilizar a variância (logaritmo dos dados)
log_serie <- (log(serie_suv))
plot(log_serie, xlab = "Ano", ylab = "Log", main = "PIB mensal em dólares - US$ (milhões)")

# Rodando o Modelo Auto
modelo_auto <- auto.arima(log_serie, trace = TRUE, stepwise = FALSE, approximation = F,max.p = 10, max.q = 10, max.P = 4, max.Q = 4)

# Trace: apresenta no console o R calculando os modelos. 
# Stepwise: seleção gradual(processo mais rápido, porém menos minucioso)
# Approximation: seleção do melhor modelo por aproximação (indicado para séries muito longas, diminui tempo computacional)
# Drift do modelo é um parâmetro que representa a tendência temporal num passeio aleatório.

# Análise dos resíduos (qualidade do modelo)
checkresiduals(modelo_auto)

plot(resid(modelo_auto))
qqnorm(resid(modelo_auto))
qqline(resid(modelo_auto))

#########################
### Examinar Residuos ###
#########################

# Teste de autocorrelação dos resíduos
#  - H0: resíduos são não autocorrelacionados
#  - H1: resíduos são autocorrelacionados
Box.test(modelo_auto$residuals,type="Ljung",lag = 24)

# Teste de heterocedasticidade condicional
#  - H0: quadrado dos resíduos são não autocorrelacionados
#  - H1: quadrado dos resíduos são autocorrelacionados
Box.test(modelo_auto$residuals^2,type="Ljung",lag = 24)

# Ho = distribuição normal : p > 0.05
# Ha = distribuição != normal : p <= 0.05
jarque.bera.test(na.remove(resid(modelo_auto)))

acf(resid(modelo_auto))
pacf(resid(modelo_auto))

################
### Previsão ###
################

# Gráfico
prev <- forecast(modelo_auto,h=12)
plot(prev)

# Valores
prev_escal <- as.data.frame(prev)^3
View(prev_escal)
