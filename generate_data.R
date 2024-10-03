install.packages("VGAM")
install.packages("dplyr")
library(VGAM)
library(dplyr)

alpha <- 1.1
x_m <- 1
num_proc <- 100

pareto <- rpareto(num_proc, scale = x_m, shape = alpha)
job_len <- pareto %>%
            ceiling()

hist(job_len)

pid <- seq(1, num_proc)

lambda <- 10
arrival <- rpois(num_proc, lambda)
arrival
hist(arrival)
jobs <- data.frame(pid, job_len, arrival)
write.csv(jobs, file = "proc2.csv", row.names = FALSE)
