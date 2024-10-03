library(tidyverse)
library(RColorBrewer)
# Round robin com 4 de quantum
# CFS com CFS(20, 4, 1)
timeline <- read.csv("results/TimelineRoundRobin.csv") %>%
  rename(t = X, pid = X0) %>%
  filter(t <= 100)

ggplot(timeline, aes(x = t, fill = factor(pid))) +
  labs(y = "pid", x = "timestamp") +
  geom_bar() + 
  theme_bw() + 
  theme(legend.position = "none")

procs <- read.csv("results/RRProc.csv")
rr_slowdown <- (procs$waiting_time + procs$cpu_time) / procs$burning_time

cfs <- read.csv("results/CFSProc2.csv")
cfs_slowdown <- (cfs$waiting_time + cfs$cpu_time) / cfs$burning_time

fifo <- read.csv("results/FifoProc.csv")
fifo_slowdown <- (fifo$waiting_time + fifo$cpu_time) / fifo$burning_time

sjf <- read.csv("results/SJFProc.csv")
sjf_slowdown <- (sjf$waiting_time + sjf$cpu_time) / sjf$burning_time

slowdown <- data.frame(rr_slowdown, cfs_slowdown, fifo_slowdown, sjf_slowdown) %>% # nolint
  rename(RoundRobin = rr_slowdown, CFS = cfs_slowdown, FIFO = fifo_slowdown, SJF = sjf_slowdown) # nolint
100 - sd(cfs_slowdown) * 100 / sd(rr_slowdown)


boxplot(slowdown, main = "Slowdown por algoritmo", ylab = "Slowdown") 

rr_response_time <- procs$response_time
cfs_response_time <- cfs$response_time
fifo_response_time <- fifo$response_time
sjf_response_time <- sjf$response_time
response_time <- data.frame(RoundRobin = rr_response_time, CFS = cfs_response_time, FIFO = fifo_response_time, SJF = sjf_response_time) # nolint

boxplot(response_time, ylab= "Response Time")

